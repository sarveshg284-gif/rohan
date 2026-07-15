import streamlit as st
from database import add_transaction


st.title("➕ Add New Transaction")


item = st.text_input(
    "ITEM"
)


quantity = st.number_input(
    "Quantity",
    min_value=1,
    step=1
)


from_location = st.text_input(
    "From Location"
)


client = st.text_input(
    "Client / Site"
)


employee = st.text_input(
    "Employee Name"
)


date = st.date_input(
    "Transaction Date"
)

status = st.selectbox(
    "STATUS",
    [
        "pending",
        "in transit",
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



if st.button("Save Transaction"):


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


        st.success(
            "Transaction Saved Successfully"
        )

    else:

        st.warning(
            "Please enter Item and Client"
        )
