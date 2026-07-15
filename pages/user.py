import streamlit as st
from database.database import *

st.title("👤 User Management")

tab1, tab2 = st.tabs(["Add User", "View Users"])

# ---------------- ADD USER ----------------

with tab1:

    with st.form("user_form"):

        fullname = st.text_input("Full Name")

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        role = st.selectbox(
            "Role",
            ["Admin", "Employee"]
        )

        submit = st.form_submit_button("Create User")

    if submit:

        add_user(
            fullname,
            username,
            password,
            role,
        )

        st.success("User Created Successfully")

# ---------------- VIEW USERS ----------------

with tab2:

    df = get_users()

    st.dataframe(
        df,
        use_container_width=True
    )

    if len(df):

        delete_id = st.number_input(
            "User ID",
            min_value=1,
            step=1
        )

        if st.button("Delete User"):

            delete_user(delete_id)

            st.success("User Deleted")

            st.rerun()
