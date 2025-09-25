import streamlit as st
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Page configuration
st.set_page_config(page_title="Health Insurance Premium Prediction", page_icon="💰", layout="centered")

# Title with custom styling
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>Health Insurance Premium Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Predict your insurance premium based on personal details</p>", unsafe_allow_html=True)
st.write("---")

# Create two columns for inputs
col1, col2 = st.columns(2)

with col1:
    age = st.number_input('Age:', min_value=0, max_value=120, value=30)
    sex = st.selectbox('Sex:', ['Male', 'Female'])
    children = st.number_input('Number of Children:', min_value=0, max_value=10, value=0)

with col2:
    bmi = st.number_input('BMI:', min_value=0.0, max_value=100.0, value=25.0, step=0.1)
    smoker = st.selectbox('Smoker:', ['Yes', 'No'])

st.write("---")

# Center the button
predict_button = st.button('Predict Premium 💵')

if predict_button:
    # Encode categorical features
    sex_encoded = 0 if sex.lower() == 'male' else 1
    smoker_encoded = 0 if smoker.lower() == 'no' else 1

    # Make prediction
    prediction = model.predict([[age, sex_encoded, bmi, children, smoker_encoded]])
    premium = round(prediction[0], 2)

    # Display the result in a styled card
    st.markdown(f"""
        <div style='background-color:#f0f8ff; padding:20px; border-radius:10px; text-align:center;'>
            <h2 style='color:#4B8BBE;'>💰 Predicted Premium</h2>
            <p style='font-size:24px; color:#FF5733;'>₹{premium}</p>
        </div>
    """, unsafe_allow_html=True)
