import streamlit as st
import pandas as pd
from database import get_transactions


st.title("📈 Reports")


df=pd.DataFrame(
get_transactions(),
columns=[
"ID",
"Item",
"Quantity",
"From",
"Client",
"Employee",
"Date",
"Remarks"
]
)


st.subheader(
"Client Wise Report"
)


client_report=df.groupby(
"Client"
)["Quantity"].sum()


st.bar_chart(
client_report
)



st.subheader(
"Employee Report"
)


employee_report=df.groupby(
"Employee"
)["Quantity"].sum()


st.line_chart(
employee_report
