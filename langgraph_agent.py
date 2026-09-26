from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from recommendation_engine import generate_recommendations
from mitigation_engine import generate_mitigations
from llm_service import generate_strategic_reasoning

class AgentState(TypedDict):
    project_data: dict
    m1_data: dict
    m2_data: dict
    recommendations: list
    mitigations: list
    strategic_reasoning: str
    is_llm_based: bool
    validation_result: str
    final_report: str

def data_ingestion(state: AgentState):
    # Simply passes through the structured inputs.
    return state
    
def risk_analysis(state: AgentState):
    # Interprets M1/M2 data using deterministic rules.
    recs = generate_recommendations(state["m1_data"], state["m2_data"])
    mits = generate_mitigations(state["m2_data"])
    return {"recommendations": recs, "mitigations": mits}
    
def strategic_reasoning_node(state: AgentState):
    context = {
        "project": state["project_data"],
        "m1": state["m1_data"],
        "m2": state["m2_data"],
        "recommendations": state["recommendations"],
        "mitigations": state["mitigations"]
    }
    
    llm_response = generate_strategic_reasoning(context)
    if llm_response.get("status") == "success":
        return {"strategic_reasoning": llm_response["reasoning"], "is_llm_based": True}
    else:
        # Deterministic fallback
        recs_titles = [r['title'] for r in state['recommendations']]
        mits_strategies = [m['strategy'] for m in state['mitigations']]
        fallback = (
            f"Deterministic Fallback Reasoning:\n"
            f"The project exhibits a risk score of {state['m2_data'].get('risk_score', 'N/A')}. "
            f"Based on key constraints, primary recommendations include {', '.join(recs_titles)}. "
            f"To mitigate core risks, focus on {', '.join(mits_strategies)}."
        )
        return {"strategic_reasoning": fallback, "is_llm_based": False}
        
def validation_node(state: AgentState):
    # Validate recommendations/mitigations and reasoning
    reasoning = state.get("strategic_reasoning", "")
    recs = state.get("recommendations", [])
    mits = state.get("mitigations", [])
    
    if len(reasoning) > 10 and len(recs) > 0 and len(mits) > 0:
        return {"validation_result": "VALID: Critical strategic components successfully generated."}
    else:
        return {"validation_result": "INVALID: Missing core strategic insights or outputs."}
        
def report_generation_node(state: AgentState):
    source = "Gemini AI" if state.get("is_llm_based") else "Deterministic Fallback"
    report = (
        f"--- Final Assessment Report ---\n"
        f"Source: {source}\n"
        f"Validation: {state['validation_result']}\n\n"
        f"Strategic Reasoning:\n{state['strategic_reasoning']}"
    )
    return {"final_report": report}
    
def run_langgraph_analysis(project_data: dict, m1_data: dict, m2_data: dict) -> dict:
    workflow = StateGraph(AgentState)
    
    workflow.add_node("data_ingestion", data_ingestion)
    workflow.add_node("risk_analysis", risk_analysis)
    workflow.add_node("strategic_reasoning", strategic_reasoning_node)
    workflow.add_node("validation", validation_node)
    workflow.add_node("report_generation", report_generation_node)
    
    workflow.set_entry_point("data_ingestion")
    workflow.add_edge("data_ingestion", "risk_analysis")
    workflow.add_edge("risk_analysis", "strategic_reasoning")
    workflow.add_edge("strategic_reasoning", "validation")
    workflow.add_edge("validation", "report_generation")
    workflow.add_edge("report_generation", END)
    
    app = workflow.compile()
    
    initial_state = {
        "project_data": project_data,
        "m1_data": m1_data,
        "m2_data": m2_data,
        "recommendations": [],
        "mitigations": [],
        "strategic_reasoning": "",
        "is_llm_based": False,
        "validation_result": "",
        "final_report": ""
    }
    
    final_state = app.invoke(initial_state)
    return final_state
