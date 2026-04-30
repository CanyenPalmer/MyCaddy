from flask import Flask, render_template, request
from my_caddy_core import get_adjusted_distance
from caddy_insights import generate_insight

app = Flask(__name__)


def get_lie_icon(lie_label, lie_quality):
    if lie_label == "Fairway" or lie_quality == "Sitting Up":
        return "___〇___"
    if lie_quality == "Sitting Down":
        return "___︵___"
    return "___⌒___"


def get_elevation_icon(elevation_direction):
    if elevation_direction == "Uphill":
        return "↑"
    if elevation_direction == "Downhill":
        return "↓"
    return "→"


def get_wind_icon(wind_dir):
    wind_icons = {
        "None": "•",
        "Into": "↓",
        "Helping": "↑",
        "Left to Right": "→",
        "Right to Left": "←",
        "Into + Left to Right": "↘",
        "Into + Right to Left": "↙",
        "Helping + Left to Right": "↗",
        "Helping + Right to Left": "↖",
    }

    return wind_icons.get(wind_dir, "•")


def get_distance_bar(base_distance, target_distance):
    base_distance = max(float(base_distance), 1)
    target_distance = max(float(target_distance), 1)

    if target_distance >= base_distance:
        visual_max = min(target_distance, base_distance * 1.15)
        base_width = (base_distance / visual_max) * 100
        target_width = 100
        extension_left = base_width
        extension_width = max(0, target_width - base_width)
        mode = "longer"
    else:
        base_width = 100
        target_width = (target_distance / base_distance) * 100
        extension_left = 0
        extension_width = target_width
        mode = "shorter"

    return {
        "mode": mode,
        "base_width": round(base_width, 2),
        "target_width": round(target_width, 2),
        "extension_left": round(extension_left, 2),
        "extension_width": round(extension_width, 2),
        "base": round(base_distance, 1),
        "target": round(target_distance, 1),
    }


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    summary = None
    insight = None
    shot_inputs = None
    distance_bar = None

    if request.method == 'POST':
        distance = float(request.form.get('distance') or 0)
        lie = float(request.form.get('lie') or 0)
        lie_quality = request.form.get('lie_quality') or 'Normal'

        elevation_feet = float(request.form.get('elevation_feet') or 0)
        elevation_direction = request.form.get('elevation_direction') or 'Flat'

        wind_speed = float(request.form.get('wind_speed') or 0)
        wind_dir = request.form.get('wind_dir') or 'None'

        temp = float(request.form.get('temperature') or 70)

        data = get_adjusted_distance(
            distance, lie, lie_quality, temp,
            wind_speed, wind_dir,
            elevation_feet, elevation_direction
        )

        insight = generate_insight(data)

        if data["lie_percent_low"] == data["lie_percent_high"]:
            lie_range_text = f"{data['lie_percent_low']}%"
        else:
            lie_range_text = f"{data['lie_percent_low']}–{data['lie_percent_high']}%"

        summary = f"Inputs → Distance: {distance} yds | Lie: {data['lie_label']} | Lie Quality: {lie_quality} | Lie Range: {lie_range_text} | Elevation: {elevation_feet} ft {elevation_direction} | Wind: {wind_speed} mph {wind_dir} | Temperature: {temp}°F"

        shot_inputs = {
            "distance": distance,
            "lie": data["lie_label"],
            "lie_quality": lie_quality,
            "lie_icon": get_lie_icon(data["lie_label"], lie_quality),
            "lie_range": lie_range_text,
            "elevation_feet": elevation_feet,
            "elevation_direction": elevation_direction,
            "elevation_icon": get_elevation_icon(elevation_direction),
            "wind_speed": wind_speed,
            "wind_dir": wind_dir,
            "wind_icon": get_wind_icon(wind_dir),
            "temperature": temp,
        }

        distance_bar = get_distance_bar(data["base"], data["final"])

        result = data

    return render_template(
        'index.html',
        result=result,
        summary=summary,
        insight=insight,
        shot_inputs=shot_inputs,
        distance_bar=distance_bar
    )


if __name__ == '__main__':
    app.run(debug=True)
