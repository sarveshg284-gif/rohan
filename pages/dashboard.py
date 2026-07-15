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
"Remarks"
]
)


col1,col2,col3=st.columns(3)


col1.metric(
"Total Transactions",
len(df)
)


col2.metric(
"Total Quantity",
df.Quantity.sum()
)


col3.metric(
"Clients",
df.Client.nunique()
)



st.subheader(
"Quantity Report"
)


st.bar_chart(
df.groupby("Item")
["Quantity"]
.sum()
)
