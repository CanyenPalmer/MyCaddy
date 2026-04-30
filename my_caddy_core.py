import math

DIAGONAL_WIND_FACTOR = math.sqrt(2) / 2


def _effective_lie_penalty_range(lie_penalty_percent, lie_quality):
    lie = float(lie_penalty_percent)

    lie_ranges = {
        0.0: {
            "label": "Fairway",
            "flyer_risk": "None",
            "Sitting Up": (0.00, 0.00),
            "Normal": (0.00, 0.00),
            "Sitting Down": (0.00, 0.00),
        },
        3.0: {
            "label": "First Cut",
            "Sitting Up": (0.01, 0.02),
            "Normal": (0.02, 0.04),
            "Sitting Down": (0.03, 0.05),
        },
        10.0: {
            "label": "Light Rough",
            "Sitting Up": (0.05, 0.07),
            "Normal": (0.07, 0.10),
            "Sitting Down": (0.10, 0.12),
        },
        20.0: {
            "label": "Rough",
            "Sitting Up": (0.09, 0.12),
            "Normal": (0.12, 0.15),
            "Sitting Down": (0.15, 0.18),
        },
        27.5: {
            "label": "Heavy Rough",
            "Sitting Up": (0.14, 0.17),
            "Normal": (0.17, 0.20),
            "Sitting Down": (0.20, 0.25),
        },
    }

    closest_lie = min(lie_ranges.keys(), key=lambda x: abs(x - lie))
    lie_data = lie_ranges[closest_lie]

    label = lie_data["label"]
    low, high = lie_data.get(lie_quality, lie_data["Normal"])

    if label == "Fairway":
        flyer_risk = "None"
    elif lie_quality == "Sitting Up":
        flyer_risk = "High"
    elif lie_quality == "Sitting Down":
        flyer_risk = "Low"
    else:
        flyer_risk = "Medium"

    return low, high, label, flyer_risk


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
    lie_quality,
    temp,
    weather,
    wind_speed,
    wind_dir,
    elevation_feet,
    elevation_direction
):
    d = float(distance)

    lie_low_eff, lie_high_eff, lie_label, flyer_risk = _effective_lie_penalty_range(lie, lie_quality)

    lie_low_adj = d * lie_low_eff
    lie_high_adj = d * lie_high_eff
    lie_mid_adj = (lie_low_adj + lie_high_adj) / 2

    elev_adj = _elevation_adjustment(elevation_feet, elevation_direction)
    wind_adj = _wind_adjustment(d, wind_speed, wind_dir)
    temp_adj = _temperature_adjustment(d, temp)
    weather_adj = _weather_adjustment(d, weather)

    base_adjusted = d + elev_adj + wind_adj - temp_adj + weather_adj

    final_low = round(base_adjusted + lie_low_adj, 1)
    final_high = round(base_adjusted + lie_high_adj, 1)
    final = round((final_low + final_high) / 2, 1)

    result = {
        "final": final,
        "final_low": final_low,
        "final_high": final_high,
        "base": d,
        "lie": round(lie_mid_adj, 1),
        "lie_low": round(lie_low_adj, 1),
        "lie_high": round(lie_high_adj, 1),
        "lie_label": lie_label,
        "lie_quality": lie_quality,
        "flyer_risk": flyer_risk,
        "elevation": round(elev_adj, 1),
        "wind": round(wind_adj, 1),
        "temperature": round(-temp_adj, 1),
        "weather": round(weather_adj, 1),
        "lie_input": lie
    }

    if flyer_risk == "High":
        result["flyer_range"] = (
            round(final * 0.90, 1),
            round(final * 0.95, 1)
        )
        result["flyer_stock"] = round((result["flyer_range"][0] + result["flyer_range"][1]) / 2, 1)

    return result
