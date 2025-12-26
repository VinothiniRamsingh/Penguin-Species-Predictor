import streamlit as st
import requests
import pandas as pd

BACKEND_URL = "http://localhost:8000/predict"  

# BACKEND_URL = "http://backend:8000/predict"


st.title("🐧 Penguin Species Predictor")
st.info("Predict penguin species using a FastAPI backend")

with st.sidebar:
    st.header("Input Features")
    island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])
    sex = st.selectbox("Sex", ["male", "female"])
    bill_length_mm = st.slider("Bill length (mm)", 32.1, 59.6, 43.9)
    bill_depth_mm = st.slider("Bill depth (mm)", 13.1, 21.5, 17.2)
    flipper_length_mm = st.slider("Flipper length (mm)", 172.0, 231.0, 201.0)
    body_mass_g = st.slider("Body mass (g)", 2700.0, 6300.0, 4207.0)

if st.button("Predict"):
    payload = {
        "island": island,
        "sex": sex,
        "bill_length_mm": bill_length_mm,
        "bill_depth_mm": bill_depth_mm,
        "flipper_length_mm": flipper_length_mm,
        "body_mass_g": body_mass_g
    }

    response = requests.post(BACKEND_URL, json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Species: **{result['species']}**")

        df = pd.DataFrame([result["probabilities"]])
        st.bar_chart(df)
    else:
        st.error("Prediction failed")
