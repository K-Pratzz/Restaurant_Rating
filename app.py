import numpy as np
import pandas as pd
import joblib
import streamlit as st

model = joblib.load("model.pkl")

st.title("🍽️ Restaurant Rating Predictor")

# Inputs
longitude = st.number_input("Longitude")
latitude = st.number_input("Latitude")

table_booking = st.selectbox("Table Booking", ["No", "Yes"])
online_delivery = st.selectbox("Online Delivery", ["No", "Yes"])
delivering_now = st.selectbox("Delivering Now", ["No", "Yes"])

price_range = st.selectbox("Price Range", [1,2,3,4])
cost = st.number_input("Cost for Two (USD)")
cuisine_count = st.number_input("Number of Cuisines")
votes = st.number_input("Votes")

# Convert to model format
table_booking = 1 if table_booking == "Yes" else 0
online_delivery = 1 if online_delivery == "Yes" else 0
delivering_now = 1 if delivering_now == "Yes" else 0

log_votes = np.log1p(votes)

# Create dataframe in SAME ORDER
input_df = pd.DataFrame([[
    longitude,
    latitude,
    table_booking,
    online_delivery,
    delivering_now,
    price_range,
    cost,
    cuisine_count,
    log_votes
]], columns=[
    'Longitude',
    'Latitude',
    'Has Table booking',
    'Has Online delivery',
    'Is delivering now',
    'Price range',
    'Cost_USD',
    'Cuisine_Count',
    'Log_Votes'
])
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Rating: {prediction[0]:.2f}")