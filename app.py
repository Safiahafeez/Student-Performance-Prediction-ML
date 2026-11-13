
import streamlit as st
import pandas as pd
import joblib

# Loading Saved Model
bundle = joblib.load("best_student_model.joblib")
model = bundle["model"]

st.title("Student Pass/Fail Prediction")

st.warning(
    "Important: This is synthetic classroom data. Predictions are for demonstration and must not be used to judge or penalize real students."
)

# Collecting Student Information
hours_studied = st.number_input(
    "Hours Studied", min_value=0.0, max_value=24.0, value=5.0
)

attendance = st.number_input(
    "Attendance (%)", min_value=0, max_value=100, value=80
)

practice_tests = st.number_input(
    "Practice Tests", min_value=0, value=3
)

sleep_hours = st.number_input(
    "Sleep Hours", min_value=0.0, max_value=24.0, value=7.0
)

study_method = st.text_input(
    "Study Method", value="Self-study"
)

# Creating Input DataFrame
input_data = pd.DataFrame([{
    "hours_studied": hours_studied,
    "attendance": attendance,
    "practice_tests": practice_tests,
    "sleep_hours": sleep_hours,
    "study_method": study_method
}])

# Predicting Student Result
if st.button("Predict Result"):
    input_data = input_data[bundle["feature_columns"]]
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("Predicted Result: Passed")
    else:
        st.warning("Predicted Result: Failed")
