import streamlit as st

st.title("📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Transactions", 520)
col2.metric("Pending", 18)
col3.metric("Delivered", 495)
col4.metric("Today's Delivery", 7)

st.divider()

st.subheader("Monthly Transaction Chart")

st.bar_chart({
    "Transactions":[20,35,40,55,70,62,90]
})
