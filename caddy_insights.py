def generate_insight(data):
    contributions = {
        "wind": abs(data["wind"]),
        "lie": abs(data["lie"]),
        "elevation": abs(data["elevation"]),
        "temperature": abs(data["temperature"]),
        "weather": abs(data["weather"])
    }

    top = sorted(contributions, key=contributions.get, reverse=True)
    primary = top[0]
    secondary = top[1]

    direction = "longer" if data["final"] > data["base"] else "shorter"

    phrases = {
        "wind_longer": "This one's playing into the wind.",
        "wind_shorter": "This one's helping.",
        "lie_longer": "That lie is going to take some off it.",
        "elevation_longer": "Uphill adds a few.",
        "elevation_shorter": "Downhill takes some off.",
        "temperature_longer": "Cool air is holding it up.",
        "temperature_shorter": "Warm air will let it fly.",
    }

    if primary == "wind":
        return phrases["wind_longer"] if direction == "longer" else phrases["wind_shorter"]

    if primary == "lie":
        return phrases["lie_longer"]

    if primary == "elevation":
        return phrases["elevation_longer"] if direction == "longer" else phrases["elevation_shorter"]

    if primary == "temperature":
        return phrases["temperature_longer"] if direction == "longer" else phrases["temperature_shorter"]

    return "This one should play close to the number."
