import streamlit as st
import pandas as pd
from database import get_transactions,delete_transaction


st.title("📋 Transactions")


rows=get_transactions()



df=pd.DataFrame(
rows,
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



start=st.date_input(
"From Date"
)


end=st.date_input(
"To Date"
)



df["Date"]=pd.to_datetime(
df["Date"]
)


df=df[
(df.Date>=pd.to_datetime(start))
&
(df.Date<=pd.to_datetime(end))
]



search=st.text_input(
"Search Item"
)



if search:

    df=df[
    df.Item.str.contains(
        search,
        case=False
    )
    ]



st.dataframe(
df,
use_container_width=True
)



excel=df.to_excel(
index=False
)



st.download_button(
"📥 Download Excel",
excel,
"transactions.xlsx"
)



delete_id=st.number_input(
"Delete ID",
min_value=1
)



if st.button("Delete"):

    delete_transaction(
        delete_id
    )

    st.rerun()
