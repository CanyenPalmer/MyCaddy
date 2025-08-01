# my_caddy_core.py

def get_real_distance(
    flag_distance_yards,
    lie_condition_percent,
    temperature_f,
    weather_condition,
    wind_direction,
    wind_speed_mph,
    shot_direction
):
    flag_distance_m = flag_distance_yards * 0.9144

    lie_penalty = lie_condition_percent / 100
    lie_effect = 1 - (0.4 * lie_penalty)

    temp_effect = 1 + ((temperature_f - 70) * 0.003)

    weather_factors = {
        "Sunny": 1.0,
        "Cloudy": 0.99,
        "Rain": 0.96,
        "Snow": 0.92
    }
    weather_effect = weather_factors.get(weather_condition, 1.0)

    direction_map = {
        "North": 0,
        "Northeast": 45,
        "East": 90,
        "Southeast": 135,
        "South": 180,
        "Southwest": 225,
        "West": 270,
        "Northwest": 315
    }

    wind_deg = direction_map.get(wind_direction, 0)
    shot_deg = direction_map.get(shot_direction, 0)
    relative_angle = abs(wind_deg - shot_deg) % 360

    if relative_angle <= 45 or relative_angle >= 315:
        wind_effect = 1 + (wind_speed_mph * 0.01)
    elif 135 <= relative_angle <= 225:
        wind_effect = 1 - (wind_speed_mph * 0.01)
    else:
        wind_effect = 1.0

    adjusted_distance_m = flag_distance_m / (lie_effect * temp_effect * weather_effect * wind_effect)
    adjusted_distance_yards = adjusted_distance_m / 0.9144
    return round(adjusted_distance_yards, 1)
