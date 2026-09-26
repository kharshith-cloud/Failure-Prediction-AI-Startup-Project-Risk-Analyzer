def generate_swot(
    team_expertise: str,
    innovation_level: str,
    market_competition: str,
    resource_availability: str,
    market_research: str
) -> dict:
    swot = {
        "Strengths": [],
        "Weaknesses": [],
        "Opportunities": [],
        "Threats": []
    }
    
    # Strengths
    if team_expertise.lower() == "high":
        swot["Strengths"].append("Strong technical team")
    if innovation_level.lower() == "high":
        swot["Strengths"].append("High innovation potential")
    if resource_availability.lower() == "good":
        swot["Strengths"].append("Good resource availability")
        
    # Weaknesses
    if team_expertise.lower() == "low":
        swot["Weaknesses"].append("Limited technical expertise")
    if market_research.lower() == "limited":
        swot["Weaknesses"].append("Limited market research")
    if resource_availability.lower() == "limited":
        swot["Weaknesses"].append("Limited resources")
        
    # Opportunities
    if market_competition.lower() == "low":
        swot["Opportunities"].append("Low market competition")
    swot["Opportunities"].append("Potential for market expansion")
    swot["Opportunities"].append("Partnership opportunities")
    
    # Threats
    if market_competition.lower() == "high":
        swot["Threats"].append("Strong competitors")
    swot["Threats"].append("Rapid technology changes")
    swot["Threats"].append("Market uncertainty")
    
    return swot
