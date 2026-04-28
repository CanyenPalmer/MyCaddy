import math


DIAGONAL_WIND_FACTOR = math.sqrt(2) / 2


def _effective_lie_penalty(lie_penalty_percent):
    lie = max(0.0, min(float(lie_penalty_percent), 100.0))

    lie_curve = [
        (0.0, 0.00),
        (10.0, 0.06),
        (25.0, 0.12),
        (50.0, 0.22),
        (75.0, 0.30),
        (100.0, 0.40),
    ]

    for i in range(len(lie_curve) - 1):
        x0, y0 = lie_curve[i]
        x1, y1 = lie_curve[i + 1]

        if x0 <= lie <= x1:
            t = (lie - x0) / (x1 - x0)
            return y0 + t * (y1 - y0)

    return lie_curve[-1][1]


def _elevation_adjustment(elevation_feet=0, elevation_direction="Flat"):
    try:
        feet = float(elevation_feet or 0)
    except ValueError:
        feet = 0.0

    direction = str(elevation_direction or "Flat").strip().lower()

    if direction == "uphill":
        return feet / 3.0

    if direction == "downhill":
        return -(feet / 3.0)

    return 0.0


def _temperature_adjustment(distance_yards, temperature_f):
    return float(distance_yards) * ((float(temperature_f) - 70.0) / 10.0) * 0.01


def _weather_adjustment(distance_yards, weather):
    condition = str(weather).strip().lower()

    if condition == "rainy":
        return float(distance_yards) * 0.02

    return 0.0


def _wind_component(wind_speed_mph=0, wind_direction="None"):
    try:
        speed = max(0.0, float(wind_speed_mph or 0))
    except ValueError:
        speed = 0.0

    direction = str(wind_direction or "None").strip().lower()

    if direction == "into":
        return speed

    if direction == "helping":
        return -speed

    if direction in ("left to right", "right to left"):
        return 0.0

    if direction in ("into + left to right", "into + right to left"):
        return speed * DIAGONAL_WIND_FACTOR

    if direction in ("helping + left to right", "helping + right to left"):
        return -speed * DIAGONAL_WIND_FACTOR

    return 0.0


def _wind_adjustment(distance_yards, wind_speed_mph=0, wind_direction="None"):
    d = float(distance_yards)
    wind_component_mph = _wind_component(wind_speed_mph, wind_direction)

    if d < 80:
        dist_scale = 0.60
    elif d < 130:
        dist_scale = 0.85
    elif d < 180:
        dist_scale = 1.00
    elif d < 230:
        dist_scale = 1.15
    else:
        dist_scale = 1.25

    if wind_component_mph > 0:
        coeff = 1.00 * dist_scale
    elif wind_component_mph < 0:
        coeff = 0.50 * dist_scale
    else:
        coeff = 0.0

    return (d / 100.0) * coeff * wind_component_mph


def get_adjusted_distance(
    flag_distance_yards,
    lie_penalty_percent,
    temperature_f,
    weather,
    wind_speed_mph=0,
    wind_direction="None",
    flyer=False,
    elevation_feet=0,
    elevation_direction="Flat",
):
    d = float(flag_distance_yards)

    effective_lie_penalty = _effective_lie_penalty(lie_penalty_percent)
    lie_adjustment = d * effective_lie_penalty

    elevation_adjustment = _elevation_adjustment(
        elevation_feet,
        elevation_direction
    )

    wind_adjustment = _wind_adjustment(
        d,
        wind_speed_mph,
        wind_direction
    )

    temp_adjustment = _temperature_adjustment(d, temperature_f)

    weather_adjustment = _weather_adjustment(d, weather)

    adjusted_distance = (
        d
        + lie_adjustment
        + elevation_adjustment
        + wind_adjustment
        - temp_adjustment
        + weather_adjustment
    )

    adjusted_distance = round(adjusted_distance, 1)

    if flyer:
        flyer_low = round(adjusted_distance * 0.90, 1)
        flyer_high = round(adjusted_distance * 0.95, 1)
        flyer_range = f"{flyer_low}–{flyer_high} yds"

        return f"Adjusted Carry Distance: {adjusted_distance} yds | Flyer range: {flyer_range}"

    return f"Adjusted Carry Distance: {adjusted_distance} yds"
