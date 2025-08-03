def get_adjusted_distance(flag_distance_yards, lie_penalty_percent, temperature_f, weather, wind_speed_mph, wind_direction, flyer=False):
    # Base temp adjustment: every 10°F away from 70 changes carry by ~2 yards
    temp_adjustment = (temperature_f - 70) * 0.2

    # Lie increases the required carry
    lie_adjustment = flag_distance_yards * (lie_penalty_percent / 100)

    # Weather logic (no impact as per previous direction)
    weather_adjustment = 0

    # Wind adjustment logic: headwind adds distance required, tailwind reduces it
    wind_multiplier = {
        'North': 1, 'South': -1, 'East': 0, 'West': 0
    }
    wind_factor = wind_speed_mph * wind_multiplier.get(wind_direction, 0) * 0.5

    # Calculate total required distance
    adjusted_distance = flag_distance_yards + lie_adjustment + wind_factor - temp_adjustment + weather_adjustment
    adjusted_distance = round(adjusted_distance, 1)

    # Flyer logic: if flyer is present, range of actual carry is *shorter* than required carry
    flyer_result = None
    if flyer:
        low = round(adjusted_distance * 0.90, 1)
        high = round(adjusted_distance * 0.95, 1)
        flyer_result = f"{low}–{high} yds"

    if flyer:
        return f"Adjusted Carry Distance: {adjusted_distance} yds | Flyer range: {flyer_result}"
    else:
        return f"Adjusted Carry Distance: {adjusted_distance} yds"
