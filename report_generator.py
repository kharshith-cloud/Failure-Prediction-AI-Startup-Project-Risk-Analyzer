from database import get_connection
import json

def generate_markdown_report(project_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT project_name, project_description, target_market, budget, competition, resources, objectives FROM projects WHERE id = %s", (project_id,))
        proj = cursor.fetchone()
        
        cursor.execute("SELECT target_market_summary, market_opportunity_assessment FROM market_analysis WHERE project_id = %s", (project_id,))
        mkt = cursor.fetchone()
        
        cursor.execute("SELECT risk_score, risk_status, success_probability FROM risk_assessment WHERE project_id = %s", (project_id,))
        risk = cursor.fetchone()
        
        cursor.execute("SELECT strengths, weaknesses, opportunities, threats FROM swot WHERE project_id = %s", (project_id,))
        swot_row = cursor.fetchone()
        
        cursor.execute("SELECT feasibility_score FROM feasibility WHERE project_id = %s", (project_id,))
        feas = cursor.fetchone()
        
        cursor.execute("SELECT title, priority, explanation FROM recommendations WHERE project_id = %s", (project_id,))
        recs = cursor.fetchall()
        
        cursor.execute("SELECT risk, strategy, explanation FROM mitigations WHERE project_id = %s", (project_id,))
        mits = cursor.fetchall()
        
        cursor.execute("SELECT strategic_reasoning, validation_result, final_report, is_llm_based FROM agent_reports WHERE project_id = %s", (project_id,))
        agent = cursor.fetchone()
    finally:
        cursor.close()
        conn.close()
        
    if not proj:
        return None
        
    md = f"# Failure Prediction AI - Assessment Report\n\n"
    md += f"## 1. Project Overview\n"
    md += f"- **Project Name:** {proj[0]}\n"
    md += f"- **Description:** {proj[1]}\n"
    md += f"- **Target Market:** {proj[2]}\n"
    md += f"- **Budget:** ${proj[3]}\n"
    md += f"- **Competition:** {proj[4]}\n"
    md += f"- **Resources:** {proj[5]}\n"
    md += f"- **Objectives:** {proj[6]}\n\n"
    
    if mkt:
        md += f"## 2. Market Analysis\n"
        md += f"- **Summary:** {mkt[0]}\n"
        md += f"- **Opportunity:** {mkt[1]}\n\n"
        
    if risk:
        md += f"## 3. Risk Assessment\n"
        md += f"- **Risk Score:** {risk[0]}/100\n"
        md += f"- **Status:** {risk[1]}\n"
        md += f"- **Success Probability:** {risk[2]}%\n\n"
        
    if feas:
        md += f"## 4. Feasibility\n"
        md += f"- **Feasibility Score:** {feas[0]}/100\n\n"
        
    if swot_row:
        strengths = json.loads(swot_row[0])
        weaknesses = json.loads(swot_row[1])
        opportunities = json.loads(swot_row[2])
        threats = json.loads(swot_row[3])
        md += f"## 5. SWOT Analysis\n"
        md += f"- **Strengths:** {', '.join(strengths) if strengths else 'None'}\n"
        md += f"- **Weaknesses:** {', '.join(weaknesses) if weaknesses else 'None'}\n"
        md += f"- **Opportunities:** {', '.join(opportunities) if opportunities else 'None'}\n"
        md += f"- **Threats:** {', '.join(threats) if threats else 'None'}\n\n"
        
    if recs:
        md += "## 6. AI Recommendations\n"
        for r in recs:
            md += f"- **[{r[1]}] {r[0]}**: {r[2]}\n"
        md += "\n"
        
    if mits:
        md += "## 7. Risk Mitigations\n"
        for m in mits:
            md += f"- **Risk:** {m[0]}\n  **Strategy:** {m[1]}\n  **Explanation:** {m[2]}\n"
        md += "\n"
        
    if agent:
        source = 'Gemini AI' if agent[3] else 'Deterministic Fallback'
        md += f"## 8. Strategic Reasoning ({source})\n"
        md += f"{agent[0]}\n\n"
        md += f"### Validation\n{agent[1]}\n"
        
    return md
