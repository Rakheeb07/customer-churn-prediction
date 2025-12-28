import streamlit as st
import joblib
import numpy as np

model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

THRESHOLD = 0.35   # change to your best threshold

st.title("Customer Churn Prediction")

age = st.number_input("Age", 10, 100, 40)
gender = st.selectbox("Gender", ["Male","Female"])
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
tenure = st.number_input("Tenure (months)", 0, 120, 12)

gender = 1 if gender=="Female" else 0

features = np.array([[age, gender, monthly, tenure]])
features = scaler.transform(features)

proba = model.predict_proba(features)[0][1]

if proba > THRESHOLD:
    st.error(f"Churn Likely 🚨 | Probability = {proba:.2f}")
else:
    st.success(f"Customer Safe 🙂 | Probability = {proba:.2f}")