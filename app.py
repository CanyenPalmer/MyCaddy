from flask import Flask, render_template, request
from my_caddy_core import get_adjusted_distance
from caddy_insights import generate_insight

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    summary = None
    insight = None

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

        result = data

    return render_template('index.html', result=result, summary=summary, insight=insight)


if __name__ == '__main__':
    app.run(debug=True)
