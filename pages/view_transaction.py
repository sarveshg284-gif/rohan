import streamlit as st
import pandas as pd
from database import get_transactions,delete_transaction


st.title("📋 View Transactions")


data = get_transactions()



df = pd.DataFrame(
data,
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



search = st.text_input(
"Search Item"
)


if search:

    df = df[
        df["Item"]
        .str.contains(
            search,
            case=False
        )
    ]



col1,col2 = st.columns(2)


with col1:

    start = st.date_input(
        "From Date"
    )


with col2:

    end = st.date_input(
        "To Date"
    )



df["Date"] = pd.to_datetime(
    df["Date"]
)


df = df[
(df["Date"] >= pd.to_datetime(start))
&
(df["Date"] <= pd.to_datetime(end))
]



st.dataframe(
df,
use_container_width=True
)



excel = df.to_excel(
    index=False
)



st.download_button(
"📥 Export Excel",
excel,
"transactions.xlsx"
)



st.subheader(
"Delete Transaction"
)


delete_id = st.number_input(
"Enter ID",
min_value=1
)


if st.button("Delete"):

    delete_transaction(
        delete_id
    )

    st.success(
        "Deleted"
    )

    st.rerun()
