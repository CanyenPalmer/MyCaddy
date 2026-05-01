def _window_text(data):
    if data["final_low"] == data["final_high"]:
        return f"{data['final']}"

    return f"{data['final_low']}–{data['final_high']}"


def _shot_direction(data):
    if data["final"] > data["base"] + 1:
        return "longer"

    if data["final"] < data["base"] - 1:
        return "shorter"

    return "stock"


def _largest_factor(data):
    factors = {
        "wind": abs(data["wind"]),
        "lie": abs(data["lie"]),
        "elevation": abs(data["elevation"]),
        "temperature": abs(data["temperature"]),
    }

    return max(factors, key=factors.get)


def _generate_base_insight(data):
    lie_label = data.get("lie_label", "Fairway")
    lie_quality = data.get("lie_quality", "Normal")
    flyer_risk = data.get("flyer_risk", "None")

    final = data["final"]
    base = data["base"]
    final_low = data["final_low"]
    final_high = data["final_high"]

    wind = data["wind"]
    elevation = data["elevation"]
    lie = data["lie"]
    temperature = data["temperature"]

    total_change = final - base
    abs_total_change = abs(total_change)
    direction = _shot_direction(data)
    primary = _largest_factor(data)
    window = _window_text(data)

    # Count strong factors
    strong_factors = 0

    if abs(wind) >= 5:
        strong_factors += 1

    if abs(lie) >= 5:
        strong_factors += 1

    if abs(elevation) >= 5:
        strong_factors += 1

    if abs(temperature) >= 3:
        strong_factors += 1

    # Near-stock shots
    if abs_total_change <= 1:
        if strong_factors >= 2:
            return "A lot working here, but it plays close to the number."
        return "Pretty stock number here. Pick your target and make a committed swing."

    if abs_total_change <= 2.5:
        if strong_factors >= 2:
            return "A lot working here, but it plays close to the number."
        return f"Not playing much different from the original number, should play {final}."

    # Complicated shots
    if strong_factors >= 3:
        return f"A few things are working on this shot. Play it around {window}."

    # Lie-first caddy reads
    if lie_label == "Fairway":
        if direction == "longer":
            return f"Clean lie, but it is playing a little longer. Play it {final}."
        if direction == "shorter":
            return f"Clean lie and it is playing shorter. Smooth swing here, do not force it."
        return "Good lie, trust the number."

    if lie_label == "First Cut":
        if lie_quality == "Sitting Up":
            if flyer_risk in ["Medium", "High", "Medium-High"]:
                return "It is sitting up in the first cut, it might come out hot."
            return "Good lie in the first cut. Should come out clean."
        if lie_quality == "Sitting Down":
            return "It's sitting down. Expect it to come out a little soft."
        return "Decent lie in the first cut, might take some spin off."

    if lie_label == "Light Rough":
        if lie_quality == "Sitting Up":
            return "Good lie in the light rough. This one can jump a bit, so swing smooth."
        if lie_quality == "Sitting Down":
            return "The ball is sitting down some. Might come up short, make sure you take enough club."
        return "Light rough here, make a committed swing."

    if lie_label == "Rough":
        if lie_quality == "Sitting Up":
            return "It's sitting up in the rough, could jump a bit."
        if lie_quality == "Sitting Down":
            return "This lie is not giving you much help. Make sure you get through it."
        return "Rough lie here. Ball-first contact is the priority."

    if lie_label == "Heavy Rough":
        if lie_quality == "Sitting Up":
            return "It is sitting up, but heavy rough is still unpredictable. Catch it clean."
        if lie_quality == "Sitting Down":
            return "Tough lie here. Do not get cute, get it in play."
        return "Heavy rough here. Take enough club to get out."

    # Primary condition reads
    if primary == "wind":
        if wind > 5:
            return f"Wind is the big factor. This is playing longer, so take enough club and flight it down."
        if wind > 0:
            return "There is a little hurt from the wind. Add just enough and commit."
        if wind < -5:
            return "Wind is helping a good bit. Take some off of it and swing smooth."
        return "The wind is helping slightly. Expect it to go a little longer."

    if primary == "elevation":
        if elevation > 5:
            return "Uphill adds some yards here. Take enough club to get up."
        if elevation > 0:
            return "A little uphill here. Should only add a few yards at most."
        if elevation < -5:
            return "Shot plays way downhill here. Take some off it or club down."
        return "Slight downhill help. It's gonna play a bit shorter to the number."

    if primary == "lie":
        if lie > 8:
            return "The lie is hurting the most. Make sure you have enough club."
        return "The lie is the main concern. Trust the number and make clean contact."

    if primary == "temperature":
        if temperature > 0:
            return "Cold today so it'll play a little longer."
        return "It's hot out, should play a little shorter."

    # Final fallback
    if direction == "longer":
        return f"This is playing a little longer than the number. Treat it like {final}."

    if direction == "shorter":
        return f"This is playing shorter than the number. Take a little off and hit it {final}."

    return "Good number here. Pick a target and swing freely."


def generate_insight(data):
    insight = _generate_base_insight(data)

    lie_label = data.get("lie_label", "Fairway")
    flyer_risk = data.get("flyer_risk", "None")

    if flyer_risk in ["Medium", "Medium-High", "High"] and lie_label != "Fairway":
        flyer_note = "Might catch a flyer with this lie."

        if flyer_note not in insight:
            insight = f"{insight} {flyer_note}"

    return insight
