import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("decision_tree_model.pkl")

st.title("Bank Marketing Predictor")
st.write("Will the customer subscribe to a term deposit?")

# Inputs
age = st.slider("Age", 18, 95, 30)
job = st.selectbox("Job", ['admin.', 'technician', 'services', 'management', 'retired',
                            'blue-collar', 'unemployed', 'entrepreneur', 'housemaid', 'student', 'self-employed'])
marital = st.selectbox("Marital", ['married', 'single', 'divorced'])
education = st.selectbox("Education", ['secondary', 'tertiary', 'primary', 'unknown'])
default = st.selectbox("Has credit in default?", ['no', 'yes'])
housing = st.selectbox("Has housing loan?", ['no', 'yes'])
loan = st.selectbox("Has personal loan?", ['no', 'yes'])

# Mapping
job_map = {'admin.': 0, 'technician': 1, 'services': 2, 'management': 3, 'retired': 4,
           'blue-collar': 5, 'unemployed': 6, 'entrepreneur': 7, 'housemaid': 8, 'student': 9, 'self-employed': 10}
marital_map = {'married': 0, 'single': 1, 'divorced': 2}
education_map = {'secondary': 0, 'tertiary': 1, 'primary': 2, 'unknown': 3}
binary_map = {'no': 0, 'yes': 1}

input_data = pd.DataFrame({
    'age': [age],
    'job': [job_map[job]],
    'marital': [marital_map[marital]],
    'education': [education_map[education]],
    'default': [binary_map[default]],
    'housing': [binary_map[housing]],
    'loan': [binary_map[loan]]
})

if st.button("Predict"):
    prediction = model.predict(input_data)
    result = "✅ Will Subscribe" if prediction[0] == 1 else "❌ Will Not Subscribe"
    st.success(f"Prediction: {result}")
