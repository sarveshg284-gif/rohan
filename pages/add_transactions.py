import streamlit as st
from database import add_transaction

st.title("➕ Add New Transaction")

with st.form("transaction_form", clear_on_submit=True):

    item = st.text_input("ITEM")

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        step=1
    )

    from_location = st.text_input("From Location")

    client = st.text_input("Client / Site")

    employee = st.text_input("Client Name")

    date = st.date_input("Transaction Date")

    status = st.selectbox(
        "STATUS",
        [
            "Pending",
            "In Transit",
            "Delivered"
        ]
    )

    remarks = st.selectbox(
        "Remarks",
        [
            "✔️",
            "❌"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:
        save = st.form_submit_button("💾 Save")

    with col2:
        save_next = st.form_submit_button("💾 Save & Next")

if save or save_next:

    if item and client:

        add_transaction(
            item,
            quantity,
            from_location,
            client,
            employee,
            str(date),
            status,
            remarks
        )

        if save:
            st.success("✅ Transaction saved successfully.")

        if save_next:
            st.success("✅ Transaction saved. Enter the next transaction below.")

    else:
        st.warning("Please enter both Item and Client.")
