def calculate_feasibility(
    market_opportunity: float,
    team_capability: float,
    competitive_advantage: float,
    resource_availability: float
) -> int:
    average = (market_opportunity + team_capability + competitive_advantage + resource_availability) / 4
    return round(average)
