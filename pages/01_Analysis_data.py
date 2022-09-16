import streamlit as st
import pandas as pd

st.title('Analysis of data')
st.header('1 Introduction to analysis of data')

# load csv
st.text('Load csv')
df = pd.read_csv("/home/luitro/repository/streamlit_tuto/curso/curso_data_science/Secciones/Seccion3.Intro_a_Data_Science/Intro_a_Pandas/primary_results.csv")

st.dataframe(df)


