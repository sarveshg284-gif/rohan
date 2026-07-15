import streamlit as st
import pandas as pd

st.title("📋 Transactions")

search = st.text_input("Search")

status = st.selectbox(
    "Status",
    ["All","Pending","In Transit","Delivered"]
)

data = pd.DataFrame({
    "ID":[1,2],
    "Description":["Laptop","Printer"],
    "Quantity":[5,2],
    "Client":["ABC Ltd","XYZ Ltd"],
    "Status":["Delivered","Pending"]
})

st.dataframe(data, use_container_width=True)
