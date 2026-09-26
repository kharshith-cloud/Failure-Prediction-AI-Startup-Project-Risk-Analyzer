def generate_mitigations(m2_data: dict) -> list:
    mits = []
    
    comp = m2_data.get("market_competition", "").lower()
    resources = m2_data.get("resource_availability", "").lower()
    team = m2_data.get("team_expertise", "").lower()
    innovation = m2_data.get("innovation_level", "").lower()
    
    if comp == "high":
        mits.append({
            "risk": "High Competition",
            "strategy": "Differentiation Strategy",
            "explanation": "Focus on unique value propositions to avoid direct price wars with incumbents."
        })
        
    if resources == "limited":
        mits.append({
            "risk": "Budget Constraints",
            "strategy": "Revenue Acceleration",
            "explanation": "Prioritize high-margin, quick-win sales channels to boost early cash flow."
        })
        
    if team == "low":
        mits.append({
            "risk": "Team Skills Gap",
            "strategy": "Strategic Hiring",
            "explanation": "Recruit experienced advisors or senior hires to cover critical technical/business gaps."
        })
        
    if innovation == "low":
        mits.append({
            "risk": "Technical Risk",
            "strategy": "Prototype and Technical Validation",
            "explanation": "Build a technical proof-of-concept to de-risk the core product architecture."
        })
        
    if not mits:
        mits.append({
            "risk": "Standard Operational Risks",
            "strategy": "Iterative Monitoring",
            "explanation": "Maintain regular risk assessment cycles as the project scales."
        })
        
    return mits
