import joblib
import pandas as pd
import numpy as np
from datetime import datetime

# Load resources
model = joblib.load('traffic_model_final.pkl')
scaler = joblib.load('scaler.pkl')

model_features = [
    'avg_vehicle_speed', 'vehicle_count_cars', 'vehicle_count_trucks', 
    'vehicle_count_bikes', 'temperature', 'humidity', 'hour', 'day_of_week',
    'weather_condition_Foggy', 'weather_condition_Rainy', 
    'weather_condition_Sunny', 'weather_condition_Windy',
    'signal_status_Red', 'signal_status_Yellow'
]

def test_scenario(speed, cars, trucks, bikes, label):
    input_dict = {
        'avg_vehicle_speed': speed, 'vehicle_count_cars': cars,
        'vehicle_count_trucks': trucks, 'vehicle_count_bikes': bikes,
        'temperature': 28, 'humidity': 75, 'hour': 17, 'day_of_week': 0,
        'weather_condition_Foggy': 0, 'weather_condition_Rainy': 0,
        'weather_condition_Sunny': 0, 'weather_condition_Windy': 1,
        'signal_status_Red': 0, 'signal_status_Yellow': 1
    }
    input_df = pd.DataFrame([input_dict])[model_features]
    input_scaled = scaler.transform(input_df)
    res = model.predict(input_scaled)[0]
    with open("output.txt", "a") as f:
        f.write(f"Scenario {label}: Pred={res:.2f} (Speed={speed}, C={cars}, T={trucks}, B={bikes})\n")

open("output.txt", "w").close() # Clear file
test_scenario(20, 250, 50, 500, "D")
