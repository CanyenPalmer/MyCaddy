def get_adjusted_distance(flag_distance_yards, lie_penalty_percent, temperature_f, weather, wind_speed_mph, wind_direction, flyer=False):
    """
    Returns the adjusted carry distance required to hit a shot based on environmental and lie conditions.
    If flyer is True, it also provides a shorter actual carry range due to unintended flyer effect.
    """

    # 1. Temperature Adjustment: ~0.2 yards per degree from 70°F
    temp_adjustment = (temperature_f - 70) * 0.2

    # 2. Lie Penalty: increases the required distance to reach the target
    lie_adjustment = flag_distance_yards * (lie_penalty_percent / 100)

    # 3. Weather Adjustment: currently set to zero (can be changed in future logic)
    weather_adjustment = 0

    # 4. Wind Adjustment: + for headwind, - for tailwind
    wind_multiplier = {
        'North': 1,  # Headwind
        'South': -1, # Tailwind
        'East': 0,   # Crosswind
        'West': 0    # Crosswind
    }
    wind_factor = wind_speed_mph * wind_multiplier.get(wind_direction, 0) * 0.5

    # 5. Final adjusted carry distance (required to reach flag)
    adjusted_distance = flag_distance_yards + lie_adjustment + wind_factor - temp_adjustment + weather_adjustment
    adjusted_distance = round(adjusted_distance, 1)

    # 6. Flyer logic: player must hit less than this number to avoid overshooting
    if flyer:
        flyer_low = round(adjusted_distance * 0.90, 1)
        flyer_high = round(adjusted_distance * 0.95, 1)
        flyer_range = f"{flyer_low}–{flyer_high} yds"
        return f"Adjusted Carry Distance: {adjusted_distance} yds | Flyer range: {flyer_range}"
    else:
        return f"Adjusted Carry Distance: {adjusted_distance} yds"
