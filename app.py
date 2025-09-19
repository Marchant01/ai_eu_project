import streamlit as st
import pandas as pd
from joblib import load

model = load("best_model.pkl")
df = pd.read_excel("pstw_dataset.xlsx", sep=";")


name = st.text_input("Namn på projektet:")
geographical_extent = st.selectbox("Geographical extent:", df["Geographical extent"].unique())
COFOG1 = st.selectbox("COFOG1-kod:", df["Functions of Goverment (COFOG level I)"].unique())
COFOG2 = st.selectbox("COFOG2-kod:", df["Functions of Goverment (COFOG level II)"].unique())
process_type = st.selectbox("Typ av process:", df["Process type"].unique())
application_type = st.selectbox("Typ av ansökan:", df["Application type"].unique())
cross_border = st.selectbox("Gränsöverskridande:", ["Ja", "Nej"])
cross_sector = st.selectbox("Tvärsektoriell:", ["Ja", "Nej"])
interaction = st.selectbox("Interaktion:", df["Interaction"].unique())
PSI_and_services = st.checkbox("PSI and services:", value=False)
imporove_managment = st.checkbox("Improve managment:", value=False)
process_and_systems = st.checkbox("Process and systems:", value=False)
ai_class1 = st.selectbox("AI classification 1:", df["AI classification (I)"].unique())
ai_class2_main = st.selectbox("AI classification 2 main:", df["AI classification (II) (main)"].unique())
ai_class2_other = st.selectbox("AI classification 2 other:", df["AI classification (II) (other I)"].unique())
keywords = st.selectbox("AI Keywords:", df["AI Keywords"].unique())
collaboration_type = st.selectbox("Collaboration:", df["Collaboration type"].unique())
funding = st.selectbox("Funding:", df["Funding source"].unique())

if st.button("Predict Effort"):
    input_data = pd.DataFrame({
        "Geographical extent": geographical_extent,
        "Functions of Goverment (COFOG level I)": COFOG1,
        "Functions of Goverment (COFOG level II)": COFOG2,
        "Process type": process_type,
        "Application type": application_type,
        "Cross-border": [1 if cross_border == "Ja" else 0],
        "Cross-sector": [1 if cross_sector == "Ja" else 0],
        "Interaction": interaction,
        "PSI and services": [1 if PSI_and_services else 0],
        "Improve managment": [1 if imporove_managment else 0],
        "Process and systems": [1 if process_and_systems else 0],
        "AI classification (I)": ai_class1,
        "AI classification (II) (main)": ai_class2_main,
        "AI classification (II) (other I)": ai_class2_other,
        "AI Keywords": keywords,
        "Collaboration type": collaboration_type,
        "Funding source": funding
    })
    
    input_data = pd.get_dummies(input_data, dtype=int)
    prediction = model.predict(input_data)
    st.write(f"Predicted Effort: {prediction[0]:.2f} person-months")