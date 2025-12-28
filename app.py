import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

THRESHOLD = 0.35   # your tuned threshold

st.title("Customer Churn Prediction")

# ---- USER INPUT ----
age = st.number_input("Age", 10, 100, 40)
gender = st.selectbox("Gender", ["Male","Female"])
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
tenure = st.number_input("Tenure (months)", 0, 120, 12)

gender = 1 if gender=="Female" else 0

# ---- PREPARE INPUT ----
features = np.array([[age, gender, monthly, tenure]])

# ---- SCALE FIX (IMPORTANT PART) ----
required_features = scaler.n_features_in_

current = features.shape[1]

if current < required_features:
    padding = np.zeros((1, required_features - current))
    features = np.hstack((features, padding))

# ---- SCALE ----
features = scaler.transform(features)

# ---- PREDICT ----
proba = model.predict_proba(features)[0][1]

if proba > THRESHOLD:
    st.error(f"🚨 Churn Likely | Probability = {proba:.2f}")
else:
    st.success(f"😊 Customer Safe | Probability = {proba:.2f}")
