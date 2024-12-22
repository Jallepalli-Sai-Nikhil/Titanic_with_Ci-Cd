import streamlit as st
import pandas as pd
import joblib

# Load models
encoder = joblib.load("models/encoder.pkl")
scaler = joblib.load("models/scaler.pkl")
model = joblib.load("models/model.pkl")

# Streamlit app
st.title("Titanic Survival Prediction")

st.sidebar.header("Passenger Details")
gender = st.sidebar.selectbox("Gender", ("male", "female"))
age = st.sidebar.number_input("Age", min_value=0, max_value=100, value=25, step=1)
fare = st.sidebar.number_input("Fare", min_value=0.0, value=30.0, step=0.5)

if st.sidebar.button("Predict"):
    try:
        # Preprocess user input
        input_data = pd.DataFrame({
            "Sex": [gender],
            "Age": [age],
            "Fare": [fare]
        })

        # Encode and scale
        input_data["Sex"] = encoder.transform(input_data["Sex"])
        input_data[["Age", "Fare"]] = scaler.transform(input_data[["Age", "Fare"]])

        # Make prediction
        prediction = model.predict(input_data)[0]
        result = "Survived" if prediction == 1 else "Did not survive"

        # Display result
        st.success(f"The passenger {result}.")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
