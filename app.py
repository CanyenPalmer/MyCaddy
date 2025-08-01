# app.py
from flask import Flask, render_template, request
from calculator import get_real_distance

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    summary = None

    if request.method == 'POST':
        try:
            distance = float(request.form['distance'])
            lie = float(request.form['lie'])
            temp = float(request.form['temperature'])
            weather = request.form['weather']
            wind_dir = request.form['wind_dir']
            wind_speed = float(request.form['wind_speed'])
            shot_dir = request.form['shot_dir']
            flyer = 'flyer' in request.form

            base_result = get_real_distance(distance, lie, temp, weather, wind_dir, wind_speed, shot_dir)

            summary = f"Inputs → Distance: {distance} yds | Lie: {lie}% | Temp: {temp}°F | " \
                      f"Weather: {weather} | Wind: {wind_speed} mph {wind_dir} | Shot: {shot_dir}"

            if flyer:
                low = round(base_result * 0.88, 1)
                high = round(base_result * 0.95, 1)
                result = f"Flyer range: {low}–{high} yards"
            else:
                result = f"Adjusted distance: {base_result} yards"
        except:
            result = "Invalid input. Please enter numeric values."

    return render_template('index.html', result=result, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
