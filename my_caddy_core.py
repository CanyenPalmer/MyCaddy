# my_caddy_core.py

def get_adjusted_distance(
    flag_distance_yards,
    lie_penalty_percent,
    temperature_f,
    wind_speed_mph,
    wind_direction
):
    """
    Calculates adjusted distance based on lie, temperature, and wind.
    Assumes golfer is always hitting North (toward the hole).

    Parameters:
    - flag_distance_yards (float): Raw distance to target (yards).
    - lie_penalty_percent (float): % increase from lie (e.g., 10 for first cut).
    - temperature_f (float): Air temp in °F; baseline is 70°F.
    - wind_speed_mph (float): Wind speed in mph.
    - wind_direction (str): Direction wind is blowing toward (e.g., 'North' = headwind).

    Returns:
    - float: Adjusted distance (yards), rounded to 1 decimal.
    """

    adjusted_distance = flag_distance_yards

    # 1. Lie adjustment
    lie_adjustment = adjusted_distance * (lie_penalty_percent / 100)
    adjusted_distance += lie_adjustment

    # 2. Temperature adjustment: ±0.1 yards per °F from 70
    temperature_adjustment = (70 - temperature_f) * 0.1
    adjusted_distance += temperature_adjustment

    # 3. Wind adjustment
    direction = wind_direction.lower()
    if direction == "north":
        wind_adjustment = 0.9 * wind_speed_mph  # headwind
    elif direction == "south":
        wind_adjustment = -0.5 * wind_speed_mph  # tailwind
    else:
        wind_adjustment = 0.0  # crosswind or neutral

    adjusted_distance += wind_adjustment

    return round(adjusted_distance, 1)
