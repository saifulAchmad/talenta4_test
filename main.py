import streamlit as st
import pandas as pd

st.title("test")
st.text("test2")
df= pd.read_csv("umkm.csv")
st.dataframe(df)