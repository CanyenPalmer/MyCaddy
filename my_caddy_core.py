import math

def get_adjusted_distance(flag_distance_yards, lie_penalty_percent, temperature_f, weather, wind_speed_mph, wind_direction, flyer=False):
    """
    Same parameters and same string return format as your current function.
    - Asymmetric wind: headwind hurts more than tailwind helps.
    - Distance-based scaling: longer shots feel more wind (no club input needed).
    """

    # 1) Temperature Adjustment: ~0.2 yards per degree from 70°F
    temp_adjustment = (temperature_f - 70) * 0.2

    # 2) Lie Penalty
    lie_adjustment = flag_distance_yards * (lie_penalty_percent / 100.0)

    # 3) Weather Adjustment (none per your spec)
    weather_adjustment = 0.0

    # 4) Wind Adjustment (asymmetric + distance-scaled)
    direction = str(wind_direction).strip().lower()
    if direction in ("north", "n"):
        axis = 1.0   # headwind
    elif direction in ("south", "s"):
        axis = -1.0  # tailwind
    elif direction in ("east", "e", "west", "w"):
        axis = 0.0   # crosswind ignored for carry
    else:
        axis = 0.0

    wind_component_mph = wind_speed_mph * axis

    # Base coefficients (yards per mph per 100 yards)
    head_base = 1.0
    tail_base = 0.5

    # Distance-based scaling (proxy for time aloft / apex) - tweak as you like
    d = float(flag_distance_yards)
    if d < 80:        dist_scale = 0.6   # short wedges feel less wind
    elif d < 130:     dist_scale = 0.85
    elif d < 180:     dist_scale = 1.0
    elif d < 230:     dist_scale = 1.15
    else:             dist_scale = 1.25  # long irons/woods feel more wind

    if wind_component_mph > 0:      # headwind
        coeff = head_base * dist_scale
    elif wind_component_mph < 0:    # tailwind
        coeff = tail_base * dist_scale
    else:
        coeff = 0.0

    wind_adjustment = (d / 100.0) * coeff * wind_component_mph

    # 5) Final adjusted carry distance
    adjusted_distance = d + lie_adjustment + wind_adjustment - temp_adjustment + weather_adjustment
    adjusted_distance = round(adjusted_distance, 1)

    # 6) Flyer logic (unchanged UI/output)
    if flyer:
        flyer_low = round(adjusted_distance * 0.90, 1)
        flyer_high = round(adjusted_distance * 0.95, 1)
        flyer_range = f"{flyer_low}–{flyer_high} yds"
        return f"Adjusted Carry Distance: {adjusted_distance} yds | Flyer range: {flyer_range}"
    else:
        return f"Adjusted Carry Distance: {adjusted_distance} yds"