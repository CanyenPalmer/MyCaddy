def generate_insight(data):
    contributions = {
        "wind": abs(data["wind"]),
        "lie": abs(data["lie"]),
        "elevation": abs(data["elevation"]),
        "temperature": abs(data["temperature"])
    }

    top = sorted(contributions, key=contributions.get, reverse=True)
    primary = top[0]

    total_change = abs(data["final"] - data["base"])

    if total_change <= 1:
        return "Play this one true to its number."

    if total_change <= 2.5:
        return "There is not much difference in our number."

    strong_factors = 0

    if abs(data["wind"]) >= 5:
        strong_factors += 1

    if abs(data["lie"]) >= 5:
        strong_factors += 1

    if abs(data["elevation"]) >= 5:
        strong_factors += 1

    if abs(data["temperature"]) >= 3:
        strong_factors += 1

    if strong_factors >= 3:
        if data["final_low"] == data["final_high"]:
            return f"There are a lot of factors at play here. Trust the {data['final']} yard number."
        return f"There are a lot of factors at play here. Anything in the {data['final_low']}–{data['final_high']} yard window is a good number."

    lie_label = data.get("lie_label")
    lie_quality = data.get("lie_quality")

    if lie_label == "First Cut" and lie_quality == "Sitting Up":
        return "This should come out clean, maybe a touch hot."

    if lie_label == "First Cut" and lie_quality == "Sitting Down":
        return "Tricky lie here. Make a confident swing."

    if lie_label == "Light Rough" and lie_quality == "Sitting Up":
        return "We found a good lie here. This one could jump a bit."

    if lie_label == "Light Rough" and lie_quality == "Sitting Down":
        return "The ball is sitting down a bit. Expect it to come out soft."

    if lie_label == "Rough" and lie_quality == "Sitting Up":
        return "Good lie in the rough, but it could jump on you."

    if lie_label == "Rough" and lie_quality == "Sitting Down":
        return "Found a bad lie here. This will come out heavy."

    if lie_label == "Heavy Rough" and lie_quality == "Sitting Up":
        return "It is sitting up, but it is still unpredictable from here."

    if lie_label == "Heavy Rough" and lie_quality == "Sitting Down":
        return "This is a tough one. Just get it out clean."

    direction = "longer" if data["final"] > data["base"] else "shorter"

    phrases = {
        "wind_longer": "This one is playing into the wind.",
        "wind_shorter": "This one has some help from the wind.",
        "lie_longer": "That lie is going to require a little more yardage.",
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
