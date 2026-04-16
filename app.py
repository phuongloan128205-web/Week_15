import streamlit as st
import pickle

st.title("House Price Prediction")

try:
    model = pickle.load(open("model.pkl", "rb"))
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")

area = st.number_input("Area (m²)", min_value=10)
bedrooms = st.number_input("Bedrooms", min_value=1)

if st.button("Predict"):
    try:
        price = model.predict([[area, bedrooms]])[0]
        st.success(f"Predicted Price: {price:.2f}")
    except Exception as e:
        st.error(f"Prediction error: {e}")