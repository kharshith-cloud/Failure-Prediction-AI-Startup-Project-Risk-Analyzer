def calculate_risk(
    market_competition: str,
    team_expertise: str,
    resource_availability: str,
    innovation_level: str,
    market_research: str
) -> int:
    score = 0
    
    # Market Competition
    mc = market_competition.lower()
    if mc == "high":
        score += 25
    elif mc == "medium":
        score += 15
    elif mc == "low":
        score += 5
        
    # Team Expertise
    te = team_expertise.lower()
    if te == "low":
        score += 20
    elif te == "medium":
        score += 10
    elif te == "high":
        score += 5
        
    # Resource Availability
    ra = resource_availability.lower()
    if ra == "limited":
        score += 20
    elif ra == "moderate":
        score += 10
    elif ra == "good":
        score += 5
        
    # Innovation
    il = innovation_level.lower()
    if il == "low":
        score += 20
    elif il == "medium":
        score += 10
    elif il == "high":
        score += 5
        
    # Market Research
    mr = market_research.lower()
    if mr == "limited":
        score += 15
    elif mr == "moderate":
        score += 8
    elif mr == "strong":
        score += 3
        
    return min(100, score)


def get_risk_status(score: int) -> str:
    if score >= 70:
        return "HIGH RISK"
    elif score >= 40:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"


def calculate_success_probability(risk_score: int) -> int:
    return max(0, 100 - risk_score)
