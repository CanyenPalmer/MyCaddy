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


def generate_insight(data):
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

    # Near-stock shots
    if abs_total_change <= 1:
        return "Pretty stock number here. Pick your target and make a committed swing."

    if abs_total_change <= 2.5:
        return "Not much in this one. It is close to the number, so trust the yardage."

    # Complicated shots
    strong_factors = 0

    if abs(wind) >= 5:
        strong_factors += 1

    if abs(lie) >= 5:
        strong_factors += 1

    if abs(elevation) >= 5:
        strong_factors += 1

    if abs(temperature) >= 3:
        strong_factors += 1

    if strong_factors >= 3:
        return f"A few things are working on this shot. Do not overthink it—play it around {window} yards and commit."

    # Lie-first caddy reads
    if lie_label == "Fairway":
        if direction == "longer":
            return f"Clean lie, but it is playing a little longer. Play the {final} number with confidence."
        if direction == "shorter":
            return f"Clean lie and it is playing shorter. Smooth swing here—do not force it."
        return "Good lie, clean number. This is one you can trust."

    if lie_label == "First Cut":
        if lie_quality == "Sitting Up":
            if flyer_risk in ["Medium", "High", "Medium-High"]:
                return "It is sitting up in the first cut. This can come out a touch hot, so control the strike."
            return "Good lie in the first cut. Should come out pretty clean."
        if lie_quality == "Sitting Down":
            return "It is sitting down just enough to matter. Stay committed and expect it to come out a little soft."
        return "First cut lie here. Nothing scary, but make sure you catch it clean."

    if lie_label == "Light Rough":
        if lie_quality == "Sitting Up":
            return "Good lie in the light rough. This one can jump a bit, so stay smooth through it."
        if lie_quality == "Sitting Down":
            return "The ball is sitting down some. Expect a softer launch and make sure you get through the grass."
        return "Light rough here. Give it a committed swing and trust the adjusted number."

    if lie_label == "Rough":
        if lie_quality == "Sitting Up":
            return "It is sitting up in the rough. Could jump on you, so keep the strike controlled."
        if lie_quality == "Sitting Down":
            return "This lie is not giving you much help. Get through it and play the full number."
        return "Rough lie here. Ball-first contact is the priority."

    if lie_label == "Heavy Rough":
        if lie_quality == "Sitting Up":
            return "It is sitting up, but heavy rough is still unpredictable. Keep it simple and make solid contact."
        if lie_quality == "Sitting Down":
            return "Tough lie here. Do not get cute—get it out clean and take your number."
        return "Heavy rough here. Contact matters more than perfection."

    # Primary condition reads
    if primary == "wind":
        if wind > 5:
            return f"Wind is the big factor. This is playing longer, so take enough club and flight it steady."
        if wind > 0:
            return "There is a little hurt from the wind. Add just enough and stay committed."
        if wind < -5:
            return "Wind is helping a good bit. Take something off and do not chase extra speed."
        return "The wind is helping slightly. Smooth swing should cover it."

    if primary == "elevation":
        if elevation > 5:
            return "Uphill is adding real yardage here. Take enough club and finish the swing."
        if elevation > 0:
            return "A little uphill here. Add a touch and trust it."
        if elevation < -5:
            return "Downhill is taking a good amount off. Do not overclub this one."
        return "Slight downhill help. Play it a shade shorter."

    if primary == "lie":
        if lie > 8:
            return "The lie is adding most of the yardage. Make sure you have enough club to get it there."
        return "The lie is the main adjustment. Trust the number and make clean contact."

    if primary == "temperature":
        if temperature > 0:
            return "Cooler air is making this play a little longer. Take the extra yardage seriously."
        return "Warm air is helping it carry. Smooth swing and let it fly."

    # Final fallback
    if direction == "longer":
        return f"This is playing a little longer than the number. Treat it like {final} and commit."

    if direction == "shorter":
        return f"This is playing shorter than the number. Take a little off and trust {final}."

    return "Good number here. Pick the line and make your normal swing."
