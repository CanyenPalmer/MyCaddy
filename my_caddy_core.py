def get_adjusted_distance(flag_distance_yards, lie_penalty_percent, temperature_f, wind_speed_mph, wind_direction, weather='Clear', flyer=False):
    adjusted = flag_distance_yards

    # Lie penalty increases distance required
    adjusted *= 1 + (lie_penalty_percent / 100)

    # Temperature effect: +0.3% per degree above 70°F
    temp_diff = temperature_f - 70
    adjusted *= 1 + (temp_diff * 0.003)

    # Wind impact: headwind increases, tailwind decreases
    if wind_direction.lower() in ['north', 'into', 'headwind']:
        adjusted *= 1 + (wind_speed_mph / 100)
    elif wind_direction.lower() in ['south', 'downwind', 'tailwind']:
        adjusted *= 1 - (wind_speed_mph / 150)

    # Flyer condition: reduce the distance needed because the shot flies farther
    flyer_range = None
    if flyer:
        # Lower adjusted carry needed since shot will go further
        low_bound = round(adjusted * 0.95, 1)
        high_bound = round(adjusted * 0.90, 1)
        flyer_range = (high_bound, low_bound)  # Shorter than base adjusted

    return {
        'normal': round(adjusted, 1),
        'flyer_range': flyer_range
    }
