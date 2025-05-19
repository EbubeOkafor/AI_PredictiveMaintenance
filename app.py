import joblib
import streamlit as st
import numpy as np

model = joblib.load("model.joblib")

st.title('Predictive Maintenance Alert Dashboard')

Vibration = st.number_input("Enter vibration value")
Temperature = st.number_input("Enter temperature value")
Pressure = st.number_input("Enter pressure value")
RPM = st.number_input("Enter RPM value")
Runtime = st.number_input("Enter Runtime value")

if st.button("Predict Maintenance Need"):
    input_data = np.array([[Vibration, Temperature, Pressure, RPM, Runtime]])
    if any(val < 0 for val in input_data.flatten()):
        st.error('Invalid input: Value cannot be nagative!')
    elif all(val == 0 for val in input_data.flatten()):
        st.error('Machine is off: Cannot predict maintenance need.')
    else:
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.error('Maintenance Needed!')
        else:
            st.success('No Maintenance Needed')

