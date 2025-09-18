import streamlit as st
from joblib import load

model = load("best_model.pkl")
