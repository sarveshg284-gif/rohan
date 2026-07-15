import streamlit as st

st.title("⚙️ Settings")

company = st.text_input("Company Name")

address = st.text_area("Address")

theme = st.selectbox(
    "Theme",
    ["Light","Dark"]
)

if st.button("Save Settings"):
    st.success("Settings Saved")
