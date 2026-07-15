import streamlit as st
from datetime import date
from database.database import add_transaction


st.title("➕ Add Transaction")


with st.form("transaction"):

    description = st.text_input(
        "Description",
        placeholder="Example: Dell Laptop"
    )


    category = st.selectbox(
        "Category",
        [
            "Laptop",
            "Keyboard",
            "CPU",
            "Mouse",
            "Other"
        ]
    )


    quantity = st.number_input(
        "Quantity",
        min_value=1
    )


    from_location = st.text_input(
        "From Location"
    )


    client = st.text_input(
        "Client Site"
    )


    employee = st.text_input(
        "Client Name"
    )


    transaction_date = st.date_input(
        "Transaction Date",
        value=date.today()
    )


    status = st.selectbox(
        "Status",
        [
            "Pending",
            "In Transit",
            "Delivered"
        ]
    )


    remark = st.selectbox(
        "Remark",
        [
            "✔️",
            "❌"
        ]
    )


    upload = st.file_uploader(
        "Upload Document",
        type=[
            "pdf",
            "jpg",
            "png"
        ]
    )


    submit = st.form_submit_button(
        "Save"
    )


if submit:

    add_transaction(
        description,
        category,
        quantity,
        from_location,
        client,
        employee,
        "",
        str(transaction_date),
        status,
        remark
    )

    st.success(
        "Transaction Saved Successfully"
    )
