def get_adjusted_distance(flag_distance_yards, lie_penalty_percent, temperature_f, weather, wind_speed_mph, wind_direction, flyer_present=False):
    # Temperature adjustment: baseline 70°F, roughly 1% per 10°F
    temp_delta = temperature_f - 70
    temp_adjustment = flag_distance_yards * (0.01 * temp_delta / 10)

    # Lie penalty adjustment
    lie_adjustment = flag_distance_yards * (lie_penalty_percent / 100)

    # Wind adjustment (simplified: headwind reduces, tailwind increases)
    wind_multiplier = 0.005  # ~0.5% per mph
    wind_effect = 0
    if wind_direction.lower() in ["north", "into", "headwind"]:
        wind_effect = -wind_speed_mph * wind_multiplier * flag_distance_yards
    elif wind_direction.lower() in ["south", "with", "tailwind"]:
        wind_effect = wind_speed_mph * wind_multiplier * flag_distance_yards
    elif wind_direction.lower() in ["cross"]:
        wind_effect = 0  # Crosswinds not affecting carry distance for simplicity

    # Weather adjustment
    weather_adjustment = 0
    if weather.lower() == "rainy":
        weather_adjustment = -0.02 * flag_distance_yards  # Rain reduces carry ~2%
    elif weather.lower() == "humid":
        weather_adjustment = 0.005 * flag_distance_yards  # Humid air can increase carry
    elif weather.lower() == "cold":
        weather_adjustment = -0.01 * flag_distance_yards

    base_adjusted = flag_distance_yards + temp_adjustment + wind_effect + weather_adjustment - lie_adjustment

    # Flyer logic: apply 5–10% *reduction* range if flyer present
    if flyer_present:
        min_adjusted = base_adjusted * 0.90
        max_adjusted = base_adjusted * 0.95
        return f"Normal: {base_adjusted:.1f} yds | Flyer range: {min_adjusted:.1f}–{max_adjusted:.1f} yds"
    else:
        return f"Adjusted Carry Distance: {base_adjusted:.1f} yds"
