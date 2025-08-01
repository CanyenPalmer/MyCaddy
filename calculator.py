import math
import tkinter as tk
from tkinter import ttk

def get_real_distance(
    flag_distance_yards,
    lie_condition_percent,
    temperature_f,
    weather_condition,
    wind_direction,
    wind_speed_mph,
    shot_direction
):
    flag_distance_m = flag_distance_yards * 0.9144
    lie_penalty = lie_condition_percent / 100
    lie_effect = 1 - (0.1 * lie_penalty)
    temp_effect = 1 + ((temperature_f - 70) * 0.003)

    weather_factors = {
        "Sunny": 1.0,
        "Cloudy": 0.99,
        "Rain": 0.96,
        "Snow": 0.92
    }
    weather_effect = weather_factors.get(weather_condition, 1.0)

    direction_map = {
        "North": 0,
        "Northeast": 45,
        "East": 90,
        "Southeast": 135,
        "South": 180,
        "Southwest": 225,
        "West": 270,
        "Northwest": 315
    }

    wind_deg = direction_map.get(wind_direction, 0)
    shot_deg = direction_map.get(shot_direction, 0)
    relative_angle = abs(wind_deg - shot_deg) % 360

    if relative_angle <= 45 or relative_angle >= 315:
        wind_effect = 1 + (wind_speed_mph * 0.01)
    elif 135 <= relative_angle <= 225:
        wind_effect = 1 - (wind_speed_mph * 0.01)
    else:
        wind_effect = 1.0

    adjusted_distance_m = flag_distance_m / (lie_effect * temp_effect * weather_effect * wind_effect)
    adjusted_distance_yards = adjusted_distance_m / 0.9144
    return round(adjusted_distance_yards, 1)

def calculate():
    try:
        flag_distance = float(flag_entry.get())
        lie_condition = float(lie_scale.get())
        temperature = float(temp_entry.get())
        weather = weather_var.get()
        wind_direction = wind_dir_var.get()
        wind_speed = float(wind_speed_entry.get())
        shot_direction = shot_dir_var.get()

        result = get_real_distance(
            flag_distance,
            lie_condition,
            temperature,
            weather,
            wind_direction,
            wind_speed,
            shot_direction
        )
        result_label.config(text=f"Adjusted distance: {result} yards")
    except ValueError:
        result_label.config(text="Please enter valid numeric values.")

root = tk.Tk()
root.title("Golf Real Distance Calculator")
root.geometry("400x450")

# Distance
tk.Label(root, text="Distance to Flag (yards):").pack()
flag_entry = tk.Entry(root)
flag_entry.pack()

# Lie Condition
tk.Label(root, text="Lie Condition (%):").pack()
lie_scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
lie_scale.pack()

# Temperature
tk.Label(root, text="Temperature (F):").pack()
temp_entry = tk.Entry(root)
temp_entry.pack()

# Weather
tk.Label(root, text="Weather Condition:").pack()
weather_var = tk.StringVar()
weather_combo = ttk.Combobox(root, textvariable=weather_var)
weather_combo['values'] = ("Sunny", "Cloudy", "Rain", "Snow")
weather_combo.current(0)
weather_combo.pack()

# Wind Direction
tk.Label(root, text="Wind Direction:").pack()
wind_dir_var = tk.StringVar()
wind_combo = ttk.Combobox(root, textvariable=wind_dir_var)
wind_combo['values'] = ("North", "Northeast", "East", "Southeast", "South", "Southwest", "West", "Northwest")
wind_combo.current(0)
wind_combo.pack()

# Wind Speed
tk.Label(root, text="Wind Speed (mph):").pack()
wind_speed_entry = tk.Entry(root)
wind_speed_entry.pack()

# Shot Direction
tk.Label(root, text="Shot Direction:").pack()
shot_dir_var = tk.StringVar()
shot_combo = ttk.Combobox(root, textvariable=shot_dir_var)
shot_combo['values'] = ("North", "Northeast", "East", "Southeast", "South", "Southwest", "West", "Northwest")
shot_combo.current(0)
shot_combo.pack()

# Calculate Button
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result
result_label = tk.Label(root, text="Adjusted distance: -- yards", font=("Arial", 12))
result_label.pack()

root.mainloop()
