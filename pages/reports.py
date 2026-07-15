import streamlit as st

st.title("📈 Reports")

st.download_button(
    "Download Excel",
    data="Sample",
    file_name="report.xlsx"
)

st.download_button(
    "Download CSV",
    data="Sample",
    file_name="report.csv"
)
