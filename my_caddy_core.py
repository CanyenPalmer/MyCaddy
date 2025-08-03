def get_adjusted_distance(
    flag_distance_yards,
    lie_penalty_percent,
    temperature_f,
    weather,
    wind_speed_mph,
    wind_direction
):
    """
    Calculates adjusted distance based on lie, temperature, weather, and wind.
    Assumes golfer always hits North.

    Returns:
        float: Adjusted distance in yards.
    """
    adjusted_distance = flag_distance_yards

    # Lie adjustment
    adjusted_distance += adjusted_distance * (lie_penalty_percent / 100)

    # Temperature adjustment: ±0.1 yards per degree from 70°F
    temp_diff = temperature_f - 70
    adjusted_distance += temp_diff * -0.1  # +temp = shorter, -temp = longer

    # Weather penalty (optional: modify as needed)
    weather_penalties = {
        "Sunny": 0.0,
        "Cloudy": 0.01,
        "Rain": 0.02,
        "Snow": 0.05
    }
    weather_penalty = weather_penalties.get(weather, 0.0)
    adjusted_distance += adjusted_distance * weather_penalty

    # Wind adjustment
    if wind_direction.lower() == "north":  # headwind
        adjusted_distance += wind_speed_mph * 0.9
    elif wind_direction.lower() == "south":  # tailwind
        adjusted_distance -= wind_speed_mph * 0.5
    # Crosswinds (east/west) currently ignored

    return round(adjusted_distance, 1)
