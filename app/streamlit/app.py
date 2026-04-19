import os
import streamlit as st
import requests

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict/contact")

st.set_page_config(page_title="Zillow Rentals Funnel Intelligence", layout="wide")

st.title("Zillow Rentals Funnel Intelligence")
st.write("Predict the probability that a user session leads to contact.")

st.subheader("Session and Listing Inputs")

device_type = st.selectbox("Device Type", ["mobile", "desktop", "tablet"])
traffic_source = st.selectbox("Traffic Source", ["organic", "paid", "email", "direct"])
room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"])
city = st.selectbox("City", ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"])

price = st.number_input("Price", min_value=1.0, value=150.0, step=1.0)
demand_score = st.number_input("Demand Score", min_value=0.0, value=1.43, step=0.01)
availability_365 = st.slider("Availability (Days Per Year)", min_value=0, max_value=365, value=90)

click = st.selectbox("Click", [0, 1], index=1)
detail_view = st.selectbox("Detail View", [0, 1], index=1)
save = st.selectbox("Save", [0, 1], index=0)

if st.button("Predict Contact"):
    payload = {
        "device_type": device_type,
        "traffic_source": traffic_source,
        "room_type": room_type,
        "city": city,
        "price": price,
        "demand_score": demand_score,
        "availability_365": availability_365,
        "click": click,
        "detail_view": detail_view,
        "save": save
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()

        st.subheader("Prediction Result")
        st.write(f"Contact Probability: {result['contact_probability']:.4f}")
        st.write(f"Predicted Contact: {result['predicted_contact']}")
        st.write(f"Threshold Used: {result['threshold_used']:.2f}")
    else:
        st.error("API request failed. Make sure the FastAPI server is running.")