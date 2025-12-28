import streamlit as st
import numpy as np
import joblib

st.title("Customer Churn Prediction")

model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

# ---------------- USER INPUTS ----------------
age = st.number_input("Age", 10, 100, 40)

gender = st.selectbox("Gender", ["Male", "Female"])
gender_val = 1 if gender == "Female" else 0

monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
tenure = st.number_input("Tenure (months)", 0, 120, 12)

# Business inputs for original model
contract = st.selectbox("Contract Type", 
            ["Month-to-Month", "One-Year", "Two-Year"])

internet = st.selectbox("Internet Service", 
            ["No Internet", "DSL", "Fiber Optic"])

tech = st.selectbox("Tech Support", 
            ["No", "Yes"])

# --------- MANUAL FEATURE ENGINEERING ----------
total_charges = monthly * tenure   # same as dataset behavior

# One-Hot Encoding (must match training)
c_one = 1 if contract == "One-Year" else 0
c_two = 1 if contract == "Two-Year" else 0

i_dsl = 1 if internet == "DSL" else 0
i_fiber = 1 if internet == "Fiber Optic" else 0

t_yes = 1 if tech == "Yes" else 0

# --------- FINAL FEATURE ORDER ---------------
features = np.array([[
    age,
    gender_val,
    monthly,
    tenure,
    total_charges,
    c_one,
    c_two,
    i_dsl,
    i_fiber,
    t_yes
]])

# ---------- SCALE ----------
features_scaled = scaler.transform(features)

# ---------- PREDICT ----------
proba = model.predict_proba(features_scaled)[0][1]

st.write("### Prediction Result")
if proba > 0.35:
    st.error(f"🚨 Churn Likely | Probability = {proba:.2f}")
else:
    st.success(f"🙂 Customer Safe | Probability = {proba:.2f}")
