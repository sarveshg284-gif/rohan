import streamlit as st
from database import login


st.set_page_config(
    page_title="Office System",
    page_icon="📦",
    layout="wide"
)



if "user" not in st.session_state:

    st.title("🔐 Office Login")


    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )


    if st.button("Login"):

        user = login(
            username,
            password
        )


        if user:

            st.session_state.user=user

            st.success("Login Successful")

            st.rerun()

        else:

            st.error("Invalid Login")


else:

    st.sidebar.success(
        f"User: {st.session_state.user[1]}"
    )


    st.title(
        "📦 Office Transaction Management"
    )


    st.info(
        "Use sidebar pages to manage transactions"
    )


    if st.sidebar.button("Logout"):

        del st.session_state.user

        st.rerun()
