from flask import Flask, render_template, request
from my_caddy_core import get_adjusted_distance
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    summary = None

    if request.method == 'POST':
        try:
            distance = float(request.form.get('distance', 0))
            lie = float(request.form.get('lie', 0))
            temp = float(request.form.get('temperature', 70))
            weather = request.form.get('weather', 'Clear')
            wind_dir = request.form.get('wind_dir', 'North')
            wind_speed = float(request.form.get('wind_speed', 0))
            flyer = request.form.get('flyer') == 'on'

            output = get_adjusted_distance(
                flag_distance_yards=distance,
                lie_penalty_percent=lie,
                temperature_f=temp,
                weather=weather,
                wind_speed_mph=wind_speed,
                wind_direction=wind_dir,
                flyer=flyer
            )

            summary = f"Inputs → Distance: {distance} yds | Lie: {lie}% | Temp: {temp}°F | " \
                      f"Weather: {weather} | Wind: {wind_speed} mph {wind_dir} | Flyer conditions: {'Yes' if flyer else 'No'}"

            result = f"Adjusted Carry Distance: {output['normal']} yds"
            if output['flyer_range']:
                result += f" | Flyer range: {output['flyer_range'][0]}–{output['flyer_range'][1]} yds"

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('index.html', result=result, summary=summary)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
