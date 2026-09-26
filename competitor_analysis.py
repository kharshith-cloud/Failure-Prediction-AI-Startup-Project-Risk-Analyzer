def analyze_competitors(competition: str) -> dict:
    if not competition or len(competition.strip()) < 10:
        return {
            "competitor_summary": competition or "None provided",
            "identified_competitors": "Insufficient data",
            "competitive_intensity": "Unknown",
            "competitive_risks": "Unidentified risks due to lack of data",
            "industry_challenges": "Cannot assess industry challenges without competitor landscape",
            "competitive_analysis_status": "Limited"
        }
    
    comp_lower = competition.lower()
    
    # Deterministic checks
    intensity = "High" if "many" in comp_lower or "existing" in comp_lower or "established" in comp_lower else "Medium to Low (emerging market)"
    
    risks = []
    if "existing" in comp_lower or "established" in comp_lower:
        risks.append("Incumbent market share dominance")
    if "platform" in comp_lower or "app" in comp_lower:
        risks.append("High customer switching costs")
    if not risks:
        risks.append("Market saturation or lack of differentiation")
        
    industry_challenges = []
    if "delivery" in comp_lower or "logistics" in comp_lower:
        industry_challenges.append("Operational overhead and unit economics")
    if "tech" in comp_lower or "ai" in comp_lower:
        industry_challenges.append("Rapid technological obsolescence")
    if not industry_challenges:
        industry_challenges.append("Standard industry competitive forces")
        
    return {
        "competitor_summary": competition,
        "identified_competitors": "Extracted from input: " + competition[:50] + ("..." if len(competition) > 50 else ""),
        "competitive_intensity": intensity,
        "competitive_risks": ", ".join(risks),
        "industry_challenges": ", ".join(industry_challenges),
        "competitive_analysis_status": "Complete"
    }
