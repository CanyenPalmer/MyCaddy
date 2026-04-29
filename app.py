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

        elevation_feet = float(request.form.get('elevation_feet') or 0)
        elevation_direction = request.form.get('elevation_direction') or 'Flat'

        wind_speed = float(request.form.get('wind_speed') or 0)
        wind_dir = request.form.get('wind_dir') or 'None'

        temp = float(request.form.get('temperature') or 70)
        weather = request.form.get('weather') or 'Clear'
        flyer = request.form.get('flyer') == 'on'

        data = get_adjusted_distance(
            distance, lie, temp, weather,
            wind_speed, wind_dir, flyer,
            elevation_feet, elevation_direction
        )

        insight = generate_insight(data)

        summary = f"Inputs → Distance: {distance} yds | Lie: {lie}% | Elevation: {elevation_feet} ft {elevation_direction} | Wind: {wind_speed} mph {wind_dir}"

        result = data

    return render_template('index.html', result=result, summary=summary, insight=insight)


if __name__ == '__main__':
    app.run(debug=True)
