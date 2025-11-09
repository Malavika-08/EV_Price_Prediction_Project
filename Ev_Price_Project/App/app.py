import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and feature columns
model = joblib.load("../model/ev_price_model.pkl")
feature_columns = joblib.load("../model/model_features.pkl")

# UI Styling (Glassmorphism)
st.markdown("""
    <style>
    .main {
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(12px);
        border-radius: 15px;
        padding: 30px;
    }
    body {
        background-image: linear-gradient(135deg, #d9a7c7, #fffcdc);
        background-size: cover;
    }
    </style>
""", unsafe_allow_html=True)

st.title("✨ Electric Vehicle Price Predictor")
st.write("Enter the vehicle specifications below to estimate the EV price.")

# Input form
battery_capacity = st.number_input("🔋 Battery Capacity (kWh)", 30, 200)
range_km = st.number_input("🚗 Driving Range (km)", 100, 900)
acceleration = st.number_input("⚡ 0-100 km/h Acceleration (seconds)", 1.0, 15.0)
top_speed = st.number_input("🏎 Top Speed (km/h)", 100, 350)
fast_charge = st.number_input("🔌 Fast Charging Power (kW)", 30, 350)

# Prepare input for model
input_data = pd.DataFrame([[battery_capacity, range_km, acceleration, top_speed, fast_charge]],  columns=["battery_capacity_kWh", "range_km", "acceleration_0_100_s", "top_speed_kmh", "fast_charging_power_kw_dc"])

# Align columns
for col in feature_columns:
    if col not in input_data.columns:
        input_data[col] = 0  # fill missing one-hot encoded features

input_data = input_data[feature_columns]  # reorder columns

# Predict
if st.button("✨ Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Price: **₹ {prediction:,.0f}**")
