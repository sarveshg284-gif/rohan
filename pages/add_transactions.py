import streamlit as st
from database import add_transaction


st.title("➕ Add New Transaction")


# Use session state to clear form after save
if "saved" not in st.session_state:
    st.session_state.saved = False


item = st.text_input(
    "Item Description",
    key="item"
)


quantity = st.number_input(
    "Quantity",
    min_value=1,
    step=1,
    key="quantity"
)


from_location = st.text_input(
    "From Location",
    key="from_location"
)


client = st.text_input(
    "Client / Site",
    key="client"
)


employee = st.text_input(
    "Employee Name",
    key="employee"
)


date = st.date_input(
    "Transaction Date",
    key="date"
)


remarks = st.selectbox(
    "Remarks",
    [
        "Completed",
        "Pending",
        "Delivered",
        "Returned",
        "Urgent"
    ],
    key="remarks"
)



if st.button("💾 Save & Next"):

    if item and client:

        add_transaction(
            item,
            quantity,
            from_location,
            client,
            employee,
            str(date),
            remarks
        )


        st.success(
            "Transaction Saved. Enter Next Transaction."
        )


        # Clear previous values
        for key in [
            "item",
            "from_location",
            "client",
            "employee"
        ]:
            st.session_state[key] = ""


        st.rerun()


    else:

        st.warning(
            "Please enter Item Description and Client"
        )
