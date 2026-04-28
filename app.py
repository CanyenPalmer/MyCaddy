from flask import Flask, render_template, request
from my_caddy_core import get_adjusted_distance

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    summary = None

    if request.method == 'POST':
        try:
            distance = float(request.form.get('distance') or 0)
            lie = float(request.form.get('lie') or 0)

            elevation_feet = float(request.form.get('elevation_feet') or 0)
            elevation_direction = request.form.get('elevation_direction') or 'Flat'

            wind_speed = float(request.form.get('wind_speed') or 0)
            wind_dir = request.form.get('wind_dir') or 'None'

            temp = float(request.form.get('temperature') or 70)
            weather = request.form.get('weather') or 'Clear'
            flyer_enabled = request.form.get('flyer', 'off') == 'on'

            result = get_adjusted_distance(
                flag_distance_yards=distance,
                lie_penalty_percent=lie,
                temperature_f=temp,
                weather=weather,
                wind_speed_mph=wind_speed,
                wind_direction=wind_dir,
                flyer=flyer_enabled,
                elevation_feet=elevation_feet,
                elevation_direction=elevation_direction
            )

            summary = (
                f"Inputs → Distance: {distance} yds | Lie: {lie}% | "
                f"Elevation: {elevation_feet} ft {elevation_direction} | "
                f"Wind: {wind_speed} mph {wind_dir} | "
                f"Temp: {temp}°F | Weather: {weather} | "
                f"Flyer conditions: {'Yes' if flyer_enabled else 'No'}"
            )

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('index.html', result=result, summary=summary)


import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
