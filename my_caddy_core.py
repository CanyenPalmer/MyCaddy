def get_adjusted_distance(flag_distance_yards, lie_penalty_percent, temperature_f,
                          wind_speed_mph, wind_direction, weather=None, flyer=False):
    adjusted = flag_distance_yards

    # Lie adjustment
    adjusted *= (1 + lie_penalty_percent / 100.0)

    # Temperature adjustment: colder air shortens flight
    temp_diff = temperature_f - 70
    adjusted *= (1 + (temp_diff * 0.002))  # +0.2% per degree over/under 70°F

    # Weather penalty
    if weather == "Rainy":
        adjusted *= 1.02
    elif weather == "Cloudy":
        adjusted *= 1.01

    # Wind adjustment
    if wind_direction == "North":  # Headwind
        adjusted += wind_speed_mph * 0.9
    elif wind_direction == "South":  # Tailwind
        adjusted -= wind_speed_mph * 0.5
    # Crosswinds do not affect distance

    base_distance = round(adjusted, 1)

    if flyer:
        flyer_min = round(base_distance + 5, 1)
        flyer_max = round(base_distance + 15, 1)
        return f"Normal: {base_distance} yds | Flyer range: {flyer_min}–{flyer_max} yds"

    return f"Adjusted Distance: {base_distance} yards"
