import streamlit as st

st.title("➕ Add Transaction")

with st.form("transaction"):

    ###description = st.text_input("Description")

    category = st.selectbox(
        "Category",
        ["Laptop","Keyboard","CPU","Mouse","Other"]
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1
    )

    from_location = st.text_input("From Location")

    client = st.text_input("Client Site")

    employee = st.text_input("Employee Name")

    ###vehicle = st.text_input("Vehicle Number")

    status = st.selectbox(
        "Status",
        ["Pending","In Transit","Delivered"]
    )

    status = st.selectbox(
    "Remark",
    ["✔️", "❌"]
    )
        
    upload = st.file_uploader(
        "Upload Document",
        ["pdf","jpg","png"]
    )

    submit = st.form_submit_button("Save")

if submit:
    st.success("Transaction Saved Successfully")
