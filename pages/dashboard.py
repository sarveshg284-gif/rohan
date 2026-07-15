import streamlit as st
import pandas as pd
from database import get_transactions


st.title("📊 Dashboard")


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
"status",
"Remarks"
]
)



a,b,c = st.columns(3)


a.metric(
"Total Transactions",
len(df)
)


b.metric(
"Total Quantity",
df["Quantity"].sum()
)


c.metric(
"Total Clients",
df["Client"].nunique()
)



st.subheader(
"Item Quantity"
)


chart=df.groupby(
"Item"
)["Quantity"].sum()


st.bar_chart(
chart
)
