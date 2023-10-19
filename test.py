import streamlit as st
from nyoka import PMMLToSKL

# Import model from PMML file
pmml_model = PMMLToSKL("revenue_prediction_model.pmml")
pmml_model.initialize()

# Streamlit UI
st.title("Predictive Model PMML Web App")
st.write("Enter numeric values for prediction:")

input1 = st.number_input("Input 1", value=0.0)
input2 = st.number_input("Input 2", value=0.0)
input3 = st.number_input("Input 3", value=0.0)
input4 = st.number_input("Input 4", value=0.0)

if st.button("Predict"):
    # Create a dictionary with input values
    input_data = {
        "input_column_name_1": input1,
        "input_column_name_2": input2,
        "input_column_name_3": input3,
        "input_column_name_4": input4
    }

    prediction = pmml_model.predict(input_data)
    st.write("Prediction:", prediction)
