from flask import Flask, render_template, request
from my_caddy_core import get_adjusted_distance

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
            weather = request.form.get('weather', 'Unknown')
            wind_dir = request.form.get('wind_dir', 'North')
            wind_speed = float(request.form.get('wind_speed', 0))

            result = get_adjusted_distance(
                flag_distance_yards=distance,
                lie_penalty_percent=lie,
                temperature_f=temp,
                wind_speed_mph=wind_speed,
                wind_direction=wind_dir
            )

            summary = f"Inputs → Distance: {distance} yds | Lie: {lie}% | Temp: {temp}°F | " \
                      f"Weather: {weather} | Wind: {wind_speed} mph {wind_dir}"

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('index.html', result=result, summary=summary)

if __name__ == '__main__':
    app.run(debug=False)
