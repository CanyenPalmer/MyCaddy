import math

DIAGONAL_WIND_FACTOR = math.sqrt(2) / 2


def _effective_lie_penalty(lie_penalty_percent):
    lie = max(0.0, min(float(lie_penalty_percent), 50.0))

    # UPDATED LIE CURVE (more realistic + less harsh mid-range)
    lie_curve = [
        (0.0, 0.00),   # Fairway
        (5.0, 0.02),   # First Cut
        (20.0, 0.07),  # Light Rough
        (35.0, 0.12),  # Rough
        (50.0, 0.18),  # Heavy Rough
    ]

    for i in range(len(lie_curve) - 1):
        x0, y0 = lie_curve[i]
        x1, y1 = lie_curve[i + 1]
        if x0 <= lie <= x1:
            t = (lie - x0) / (x1 - x0)
            return y0 + t * (y1 - y0)

    return lie_curve[-1][1]


def _elevation_adjustment(feet, direction):
    if direction == "Uphill":
        return feet / 3
    if direction == "Downhill":
        return -(feet / 3)
    return 0


def _temperature_adjustment(d, temp):
    return d * ((temp - 70) / 10) * 0.01


def _weather_adjustment(d, weather):
    if weather.lower() == "rainy":
        return d * 0.02
    return 0


def _wind_component(speed, direction):
    if direction == "Into":
        return speed
    if direction == "Helping":
        return -speed
    if "Into +" in direction:
        return speed * DIAGONAL_WIND_FACTOR
    if "Helping +" in direction:
        return -speed * DIAGONAL_WIND_FACTOR
    return 0


def _wind_adjustment(d, speed, direction):
    comp = _wind_component(speed, direction)

    if d < 80:
        scale = 0.60
    elif d < 130:
        scale = 0.85
    elif d < 180:
        scale = 1.00
    elif d < 230:
        scale = 1.15
    else:
        scale = 1.25

    if comp > 0:
        coeff = 1.0 * scale
    elif comp < 0:
        coeff = 0.5 * scale
    else:
        coeff = 0

    return (d / 100) * coeff * comp


def get_adjusted_distance(
    distance,
    lie,
    temp,
    weather,
    wind_speed,
    wind_dir,
    flyer,
    elevation_feet,
    elevation_direction
):
    d = float(distance)

    lie_eff = _effective_lie_penalty(lie)
    lie_adj = d * lie_eff

    elev_adj = _elevation_adjustment(elevation_feet, elevation_direction)
    wind_adj = _wind_adjustment(d, wind_speed, wind_dir)
    temp_adj = _temperature_adjustment(d, temp)
    weather_adj = _weather_adjustment(d, weather)

    final = d + lie_adj + elev_adj + wind_adj - temp_adj + weather_adj
    final = round(final, 1)

    result = {
        "final": final,
        "base": d,
        "lie": round(lie_adj, 1),
        "elevation": round(elev_adj, 1),
        "wind": round(wind_adj, 1),
        "temperature": round(-temp_adj, 1),
        "weather": round(weather_adj, 1),
        "flyer": flyer,
        "lie_input": lie
    }

    # Flyer logic remains unchanged
    if flyer:
        if lie <= 35:
            result["flyer_range"] = (
                round(final * 0.90, 1),
                round(final * 0.95, 1)
            )
        else:
            result["flyer_warning"] = True

    return result
