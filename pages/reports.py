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


report=df.groupby(
"Client"
)["Quantity"].sum()


st.bar_chart(
report
)


st.subheader(
"Monthly Report"
)


df["Date"]=pd.to_datetime(
df.Date
)


monthly=df.groupby(
df.Date.dt.month
)["Quantity"].sum()


st.line_chart(
monthly
)
