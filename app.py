from flask import Flask, render_template, request, Response
from database import get_connection
import json
import time
import traceback
from market_analysis import analyze_market
from competitor_analysis import analyze_competitors
from risk_engine import calculate_risk, get_risk_status, calculate_success_probability
from swot_analysis import generate_swot
from feasibility import calculate_feasibility
from langgraph_agent import run_langgraph_analysis
from report_generator import generate_markdown_report

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_project():
    start_time = time.perf_counter()
    error_message = None
    
    try:
        # Milestone 1 Inputs - Validation
        project_name = request.form.get("project_name", "").strip()
        project_description = request.form.get("project_description", "").strip()
        target_market = request.form.get("target_market", "").strip()
        objectives = request.form.get("objectives", "").strip()
        
        if not project_name or not project_description or not target_market or not objectives:
            return render_template("index.html", error="Validation Error: Project Name, Description, Target Market, and Objectives are required.")
            
        budget_str = request.form.get("budget", "0").strip()
        if not budget_str.isdigit():
            return render_template("index.html", error="Validation Error: Budget must be a valid numeric value.")
        budget = int(budget_str)
        
        competition = request.form.get("competition", "").strip()
        resources = request.form.get("resources", "").strip()
        
        # Milestone 2 Inputs - Validation
        rm_competition = request.form.get("rm_competition", "Medium")
        rm_team = request.form.get("rm_team", "Medium")
        rm_resources = request.form.get("rm_resources", "Moderate")
        rm_innovation = request.form.get("rm_innovation", "Medium")
        rm_research = request.form.get("rm_research", "Moderate")
        
        valid_risk_levels = ["Low", "Medium", "High", "Limited", "Moderate", "Good", "Strong"]
        if any(x not in valid_risk_levels for x in [rm_competition, rm_team, rm_resources, rm_innovation, rm_research]):
            return render_template("index.html", error="Validation Error: Invalid risk dropdown selection.")
        
        try:
            f_market = float(request.form.get("f_market", 50))
            f_team = float(request.form.get("f_team", 50))
            f_comp = float(request.form.get("f_comp", 50))
            f_res = float(request.form.get("f_res", 50))
        except ValueError:
            return render_template("index.html", error="Validation Error: Feasibility inputs must be numeric.")
        
        # Analyze Milestone 1
        market_data = analyze_market(target_market)
        comp_data = analyze_competitors(competition)
        
        # Analyze Milestone 2
        risk_score = calculate_risk(rm_competition, rm_team, rm_resources, rm_innovation, rm_research)
        risk_status = get_risk_status(risk_score)
        success_prob = calculate_success_probability(risk_score)
        swot_data = generate_swot(rm_team, rm_innovation, rm_competition, rm_resources, rm_research)
        feasibility_score = calculate_feasibility(f_market, f_team, f_comp, f_res)
        
        # Pack for M3
        project_info = {
            "project_name": project_name,
            "project_description": project_description,
            "target_market": target_market,
            "budget": budget,
            "competition": competition,
            "resources": resources,
            "objectives": objectives
        }
        m1_data = {"market_data": market_data, "comp_data": comp_data, "budget": budget}
        m2_data = {
            "market_competition": rm_competition,
            "team_expertise": rm_team,
            "resource_availability": rm_resources,
            "innovation_level": rm_innovation,
            "market_research": rm_research,
            "risk_score": risk_score,
            "risk_status": risk_status,
            "feasibility_score": feasibility_score,
            "market_opportunity": f_market
        }
        
        # Analyze Milestone 3
        try:
            m3_state = run_langgraph_analysis(project_info, m1_data, m2_data)
        except Exception as e:
            print(f"LangGraph execution error: {str(e)}")
            m3_state = {
                "recommendations": [],
                "mitigations": [],
                "strategic_reasoning": "System Error: Failed to execute strategic reasoning.",
                "validation_result": "INVALID",
                "final_report": "System Error: LangGraph pipeline failure.",
                "is_llm_based": False
            }
            
        recommendations = m3_state.get("recommendations", [])
        mitigations = m3_state.get("mitigations", [])
        strategic_reasoning = m3_state.get("strategic_reasoning", "")
        validation_result = m3_state.get("validation_result", "")
        final_report = m3_state.get("final_report", "")
        is_llm_based = m3_state.get("is_llm_based", False)
        
        # Database Persistence
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            # 1. Project
            cursor.execute("""
                INSERT INTO projects (project_name, project_description, target_market, budget, competition, resources, objectives) 
                VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id
            """, (project_name, project_description, target_market, budget, competition, resources, objectives))
            project_id = cursor.fetchone()[0]
            
            # 2. Market & Competitor
            cursor.execute("""
                INSERT INTO market_analysis (project_id, target_market_summary, market_characteristics, market_opportunity_assessment, growth_potential_assessment, identified_market_challenges, market_analysis_status) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (project_id, market_data["target_market_summary"], market_data["market_characteristics"], market_data["market_opportunity_assessment"], market_data["growth_potential_assessment"], market_data["identified_market_challenges"], market_data["market_analysis_status"]))
            
            cursor.execute("""
                INSERT INTO competitor_analysis (project_id, competitor_summary, identified_competitors, competitive_intensity, competitive_risks, industry_challenges, competitive_analysis_status) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (project_id, comp_data["competitor_summary"], comp_data["identified_competitors"], comp_data["competitive_intensity"], comp_data["competitive_risks"], comp_data["industry_challenges"], comp_data["competitive_analysis_status"]))
            
            # 3. Risk, SWOT, Feasibility
            cursor.execute("""
                INSERT INTO risk_assessment (project_id, market_competition, team_expertise, resource_availability, innovation_level, market_research, risk_score, risk_status, success_probability) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (project_id, rm_competition, rm_team, rm_resources, rm_innovation, rm_research, risk_score, risk_status, success_prob))
            
            cursor.execute("""
                INSERT INTO swot (project_id, strengths, weaknesses, opportunities, threats) 
                VALUES (%s, %s, %s, %s, %s)
            """, (project_id, json.dumps(swot_data["Strengths"]), json.dumps(swot_data["Weaknesses"]), json.dumps(swot_data["Opportunities"]), json.dumps(swot_data["Threats"])))
            
            cursor.execute("""
                INSERT INTO feasibility (project_id, market_opportunity, team_capability, competitive_advantage, resource_availability, feasibility_score) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (project_id, f_market, f_team, f_comp, f_res, feasibility_score))
            
            # 4. M3 Tables
            for rec in recommendations:
                cursor.execute("""
                    INSERT INTO recommendations (project_id, title, priority, explanation) 
                    VALUES (%s, %s, %s, %s)
                """, (project_id, rec["title"], rec["priority"], rec["explanation"]))
                
            for mit in mitigations:
                cursor.execute("""
                    INSERT INTO mitigations (project_id, risk, strategy, explanation) 
                    VALUES (%s, %s, %s, %s)
                """, (project_id, mit["risk"], mit["strategy"], mit["explanation"]))
                
            cursor.execute("""
                INSERT INTO agent_reports (project_id, strategic_reasoning, validation_result, final_report, is_llm_based) 
                VALUES (%s, %s, %s, %s, %s)
            """, (project_id, strategic_reasoning, validation_result, final_report, is_llm_based))
            
            connection.commit()
        except Exception as db_e:
            if 'connection' in locals():
                connection.rollback()
            print(f"Database error: {traceback.format_exc()}")
            return render_template("index.html", error="A database error occurred while saving your project. Please try again.")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals():
                connection.close()
        
        elapsed_time = time.perf_counter() - start_time
        print(f"Submission processed in {elapsed_time:.2f} seconds.")
        
        risk_info = {"score": risk_score, "status": risk_status, "probability": success_prob}
        feasibility_info = {"market_opportunity": f_market, "team_capability": f_team, "competitive_advantage": f_comp, "resource_availability": f_res, "score": feasibility_score}
        
        return render_template(
            "result.html", 
            project_id=project_id,
            project=project_info, 
            market=market_data, 
            comp=comp_data,
            risk=risk_info,
            swot=swot_data,
            feasibility=feasibility_info,
            recommendations=recommendations,
            mitigations=mitigations,
            final_report=final_report,
            is_llm_based=is_llm_based,
            elapsed_time=round(elapsed_time, 2)
        )

    except Exception as general_e:
        print(f"Unexpected error: {traceback.format_exc()}")
        return render_template("index.html", error="An unexpected error occurred during processing. Please verify your inputs and try again.")

@app.route("/download_report/<int:project_id>")
def download_report(project_id):
    md_content = generate_markdown_report(project_id)
    if not md_content:
        return "Report not found.", 404
        
    return Response(
        md_content,
        mimetype="text/markdown",
        headers={"Content-disposition": f"attachment; filename=project_{project_id}_assessment.md"}
    )

if __name__ == "__main__":
    app.run(debug=True)
