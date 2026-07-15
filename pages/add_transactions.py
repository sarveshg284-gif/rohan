import streamlit as st
from database import add_transaction


st.title("➕ Add Transaction")


item = st.text_input("Item Description")


quantity = st.number_input(
    "Quantity",
    min_value=1
)


location = st.text_input(
    "From Location"
)


client = st.text_input(
    "Client / Site"
)


employee = st.text_input(
    "Employee Name"
)


date = st.date_input(
    "Date"
)


remarks = st.text_area(
    "Remarks"
)



if st.button("Save"):


    add_transaction(
        item,
        quantity,
        location,
        client,
        employee,
        str(date),
        remarks
    )


    st.success(
        "Transaction Added"
    )
