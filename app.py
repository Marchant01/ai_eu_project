import streamlit as st
import pandas as pd
from joblib import load
import warnings
import numpy as np

warnings.filterwarnings("ignore", message="X has feature names")

model = load("best_model.pkl")
reg_model = load("reg_model.pkl")
features = load("features.pkl")
targets = load("targets.pkl")
df = pd.read_excel("pstw_dataset.xlsx")

# Turns features to a list object
features = features.columns.tolist()

st.title("AI Project Prediction")
st.write("Welcome to the AI Project Predictor App.\n"
         + "With the help a number of key factors this application will predict if your AI project will \n "
         + "make it into implementation.\n\n Please enter the project details below:")



name = st.text_input("Name of the project")
geographical_extent = st.selectbox("Geographical extent:", df["Geographical extent"].unique())
COFOG1 = st.selectbox("COFOG1 level 1", df["Functions of Government (COFOG level I)"].unique())
COFOG2 = st.selectbox("COFOG2 level 2:", df["Functions of Government (COFOG level II)"].unique())
process_type = st.selectbox("Process type:", df["Process type"].unique())
application_type = st.selectbox("Application type:", df["Application type"].unique())
cross_border = st.selectbox("Cross border:", ["Yes", "No"])
cross_sector = st.selectbox("Cross sector:", ["Yes", "No"])
interaction = st.selectbox("Type of interaction:", df["Interaction"].unique())
PSI_and_services = st.checkbox("PSI and services:", value=False)
imporove_managment = st.checkbox("Improve managment:", value=False)
process_and_systems = st.checkbox("Process and systems:", value=False)
ai_class1 = st.selectbox("AI classification 1:", df["AI Classification (I)"].dropna().unique())
ai_class2_main = st.selectbox("AI classification 2 main:", df["AI Classification Subdomain (II) (main)"].dropna().unique())
ai_class2_other = st.selectbox("AI classification 2 other:", df["AI Classification Subdomain (II) (Other I)"].dropna().unique())
keywords = st.selectbox("AI Keywords:", df["AI Keywords"].dropna().unique())
collaboration_type = st.selectbox("Collaboration:", df["Collaboration type"].dropna().unique())
funding = st.selectbox("Funding:", df["Funding source"].dropna().unique())

status = {
        0: 'Implemented',
        1: 'In development',
        2: 'Not in use',
        3: 'Pilot',
        4: 'Planned'
}

if st.button("Predict Effort"):
    input_data = pd.DataFrame([{
        "Geographical extent": geographical_extent,
        "Functions of Government (COFOG level I)": COFOG1,
        "Functions of Government (COFOG level II)": COFOG2,
        "Process type": process_type,
        "Application type": application_type,
        "Cross-border": 1 if cross_border == "Yes" else 0,
        "Cross-sector": 1 if cross_sector == "Yes" else 0,
        "Interaction": interaction,
        "PSI and services": 1 if PSI_and_services else 0,
        "Improve management": 1 if imporove_managment else 0,
        "Process and systems": 1 if process_and_systems else 0,
        "AI classification (I)": ai_class1,
        "AI classification (II) (main)": ai_class2_main,
        "AI classification (II) (other I)": ai_class2_other,
        "AI Keywords": keywords,
        "Collaboration type": collaboration_type,
        "Funding source": funding
    }])
    
    # Encodes input data from user
    input_data = pd.get_dummies(input_data, dtype=int)
    input_data = input_data.reindex(columns=features, fill_value=0)

    # Predicts based on input data
    prediction = model.predict(input_data)
    predicted_status = status.get(prediction[0])

    # For viewing the amount and percentage of matching status
    match_count = np.sum(targets == prediction[0])
    total_count = np.size(targets)
    percentage = (match_count / total_count) * 100
    
    duration_pred_years = reg_model.predict(input_data)[0]

    st.subheader("Results")
    st.write(f"**Your project is predictet to reach the status of:** {predicted_status} "
         f"(similar to {match_count} other projects, {percentage:.1f}%)")
    st.write(f"Estimated Time to Implementation: **~{round(duration_pred_years)} years**")
