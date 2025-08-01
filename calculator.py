import math

def get_real_distance(
    flag_distance_yards,
    lie_condition_percent,
    temperature_f,
    weather_condition,
    wind_direction,
    wind_speed_mph,
    shot_direction
):
    # Convert distance to meters for physics calcs, then back later
    flag_distance_m = flag_distance_yards * 0.9144

    # --- Lie condition penalty (rough reduces carry) ---
    # Fairway = 0% penalty, buried = 100% penalty, linear approximation
    lie_penalty = lie_condition_percent / 100
    lie_effect = 1 - (0.1 * lie_penalty)  # Max 10% loss for 100% buried

    # --- Temperature effect ---
    # Ball travels ~1-2 yards less per 10°F below 70°F
    temp_effect = 1 + ((temperature_f - 70) * 0.003)  # Approx 0.3% per 10F

    # --- Weather condition effect ---
    weather_factors = {
        "sunny": 1.0,
        "cloudy": 0.99,
        "rain": 0.96,
        "snow": 0.92
    }
    weather_effect = weather_factors.get(weather_condition.lower(), 1.0)

    # --- Wind effect ---
    direction_map = {
        "north": 0,
        "northeast": 45,
        "east": 90,
        "southeast": 135,
        "south": 180,
        "southwest": 225,
        "west": 270,
        "northwest": 315
    }

    wind_deg = direction_map.get(wind_direction.lower(), 0)
    shot_deg = direction_map.get(shot_direction.lower(), 0)
    relative_angle = abs(wind_deg - shot_deg) % 360

    # Wind influence based on angle difference
    if relative_angle <= 45 or relative_angle >= 315:
        wind_effect = 1 + (wind_speed_mph * 0.01)  # tailwind
    elif 135 <= relative_angle <= 225:
        wind_effect = 1 - (wind_speed_mph * 0.01)  # headwind
    else:
        wind_effect = 1.0  # crosswind (ignoring side drift here)

    # --- Combine all effects ---
    adjusted_distance_m = flag_distance_m / (lie_effect * temp_effect * weather_effect * wind_effect)

    adjusted_distance_yards = adjusted_distance_m / 0.9144
    return round(adjusted_distance_yards, 1)

# Example usage
if __name__ == "__main__":
    # Get user input
    flag_distance = float(input("Distance to flag (yards): "))
    lie_condition = float(input("Lie condition (0-100%): "))
    temperature = float(input("Temperature (F): "))
    weather = input("Weather (sunny, cloudy, rain, snow): ")
    wind_direction = input("Wind direction (N, NE, E, SE, etc.): ")
    wind_speed = float(input("Wind speed (mph): "))
    shot_direction = input("Shot direction (N, NE, E, SE, etc.): ")

    real_distance = get_real_distance(
        flag_distance,
        lie_condition,
        temperature,
        weather,
        wind_direction,
        wind_speed,
        shot_direction
    )

    print(f"\nAdjusted (real) distance to flag: {real_distance} yards")
