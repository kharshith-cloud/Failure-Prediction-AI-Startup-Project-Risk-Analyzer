def analyze_market(target_market: str) -> dict:
    if not target_market or len(target_market.strip()) < 10:
        return {
            "target_market_summary": target_market or "None provided",
            "market_characteristics": "Insufficient data to determine characteristics",
            "market_opportunity_assessment": "Unknown",
            "growth_potential_assessment": "Cannot be assessed without detailed market data",
            "identified_market_challenges": "Data limitation",
            "market_analysis_status": "Limited"
        }
    
    market_lower = target_market.lower()
    
    # Simple deterministic characteristics
    characteristics = []
    if "student" in market_lower or "college" in market_lower or "school" in market_lower:
        characteristics.append("Education-focused demographic")
    if "tech" in market_lower or "software" in market_lower or "digital" in market_lower:
        characteristics.append("Tech-savvy user base")
    if "business" in market_lower or "b2b" in market_lower or "enterprise" in market_lower:
        characteristics.append("B2B Market")
    if not characteristics:
        characteristics.append("General consumer/niche market")
        
    opportunity = "Moderate to High based on defined target" if len(target_market) > 30 else "Moderate (requires deeper market research)"
    growth = "Scalable" if "global" in market_lower or "online" in market_lower else "Local/Regional constraints may apply"
    
    challenges = []
    if "b2b" in market_lower:
        challenges.append("Longer sales cycles")
    if "student" in market_lower:
        challenges.append("Price sensitivity")
    if not challenges:
        challenges.append("Market penetration and user acquisition")
        
    return {
        "target_market_summary": target_market,
        "market_characteristics": ", ".join(characteristics),
        "market_opportunity_assessment": opportunity,
        "growth_potential_assessment": growth,
        "identified_market_challenges": ", ".join(challenges),
        "market_analysis_status": "Complete"
    }
