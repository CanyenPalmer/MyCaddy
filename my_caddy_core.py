# my_caddy_core.py

def get_adjusted_distance(
    flag_distance_yards,
    lie_penalty_percent,
    temperature_f,
    wind_speed_mph,
    wind_direction,
    weather_condition="Sunny"
):
    """
    Calculates adjusted distance accounting for:
    - Lie penalty
    - Temperature effect
    - Wind effect (relative to golfer's fixed North-facing orientation)
    - Weather condition (e.g., rain, snow)
    """

    # Lie adjustment
    lie_multiplier = 1 + (lie_penalty_percent / 100)

    # Temperature effect: baseline at 70°F
    temp_adjustment = 1 + ((temperature_f - 70) * 0.003)

    # Weather multiplier
    weather_factors = {
        "Sunny": 1.00,
        "Cloudy": 0.99,
        "Rain": 0.96,
        "Snow": 0.92
    }
    weather_multiplier = weather_factors.get(weather_condition, 1.00)

    # Wind effect (simplified since shot is always facing North)
    if wind_direction == "North":  # Headwind
        wind_adjustment = wind_speed_mph * 0.9
    elif wind_direction == "South":  # Tailwind
        wind_adjustment = -wind_speed_mph * 0.5
    else:  # Crosswinds and others ignored
        wind_adjustment = 0

    # Base adjusted distance before wind
    adjusted_distance = flag_distance_yards * lie_multiplier * temp_adjustment * weather_multiplier

    # Apply wind impact
    final_distance = adjusted_distance + wind_adjustment

    return round(final_distance, 1)

