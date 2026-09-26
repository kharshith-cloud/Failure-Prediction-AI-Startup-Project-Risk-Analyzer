def generate_recommendations(m1_data: dict, m2_data: dict) -> list:
    recs = []
    
    comp = m2_data.get("market_competition", "").lower()
    resources = m2_data.get("resource_availability", "").lower()
    team = m2_data.get("team_expertise", "").lower()
    feasibility_score = m2_data.get("feasibility_score", 0)
    market_opportunity = m2_data.get("market_opportunity", 0)
    budget = m1_data.get("budget", 0)
    
    if comp == "high":
        recs.append({
            "title": "Competitive Positioning",
            "priority": "High",
            "explanation": "Due to high competition, focus heavily on a differentiation strategy to stand out."
        })
        
    if resources == "limited":
        recs.append({
            "title": "Secure Additional Funding",
            "priority": "Critical",
            "explanation": "Limited resources require immediate capitalization to avoid running out of runway."
        })
        
    if team == "low":
        recs.append({
            "title": "Strategic Hiring",
            "priority": "High",
            "explanation": "Low team expertise identified. Capability building and hiring key talent is crucial."
        })
        
    if feasibility_score < 60:
        recs.append({
            "title": "Develop MVP First",
            "priority": "Medium",
            "explanation": "Overall feasibility is weak. Validate assumptions with a Minimum Viable Product before scaling."
        })
        
    if market_opportunity > 60 and resources == "limited":
        recs.append({
            "title": "Build Strategic Partnership",
            "priority": "High",
            "explanation": "Good market opportunity but limited resources. Partnering can unlock growth without massive capital."
        })
        
    if budget < 10000:
        recs.append({
            "title": "Reduce Operational Costs",
            "priority": "High",
            "explanation": "Budget constraints require lean operations to maximize survival chances."
        })
        
    if not recs:
        recs.append({
            "title": "Proceed with Standard Execution",
            "priority": "Medium",
            "explanation": "No critical risk factors detected. Proceed with the current operational plan while monitoring metrics."
        })
        
    return recs
