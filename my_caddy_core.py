def get_adjusted_distance(
    flag_distance_yards,
    lie_penalty_percent,
    temperature_f,
    weather,
    wind_speed_mph,
    wind_direction,
    flyer_conditions=False
):
    """
    Calculate the adjusted carry distance accounting for lie, temperature, weather, and wind.
    Flyer conditions provide a possible flyer range, but are not included in the main result.

    - Lie increases required carry distance (e.g., lie penalty of 10% means you need to hit it 10% farther)
    - Temperature is normalized at 70°F (warmer = more carry, cooler = less)
    - Wind direction: "North" = into wind, "South" = downwind, "East"/"West" = crosswind
    - Flyer condition gives a range of flyer carry if user selects it, but does NOT affect the primary adjusted distance
    """

    # Step 1: Lie adjustment (add % to required carry)
    lie_multiplier = 1 + (lie_penalty_percent / 100.0)
    distance_with_lie = flag_distance_yards * lie_multiplier

    # Step 2: Temperature adjustment
    temp_diff = temperature_f - 70  # Normalize to 70°F
    temp_adjustment = temp_diff * 0.1  # 0.1 yard per °F
    distance_with_temp = distance_with_lie + temp_adjustment

    # Step 3: Weather (rain reduces carry slightly)
    if weather.lower() in ['rain', 'rainy']:
        weather_adjustment = -5  # reduce carry in rain
    else:
        weather_adjustment = 0
    distance_with_weather = distance_with_temp + weather_adjustment

    # Step 4: Wind
    if wind_direction.lower() == 'north':  # Into wind
        wind_adjustment = -0.5 * wind_speed_mph
    elif wind_direction.lower() == 'south':  # Downwind
        wind_adjustment = 0.5 * wind_speed_mph
    else:  # Crosswinds (East/West)
        wind_adjustment = 0
    adjusted_distance = distance_with_weather + wind_adjustment

    # Step 5: Flyer conditions (show range if checkbox selected, but not applied to main adjusted_distance)
    flyer_range = None
    if flyer_conditions:
        # Flyers fly farther, but player must still aim to hit normal carry to avoid overshooting
        # Since lie already inflates adjusted carry, this serves only as awareness
        flyer_min = adjusted_distance + 5
        flyer_max = adjusted_distance + 15
        flyer_range = (round(flyer_min, 1), round(flyer_max, 1))

    return {
        "adjusted_distance": round(adjusted_distance, 1),
        "flyer_range": flyer_range
    }
