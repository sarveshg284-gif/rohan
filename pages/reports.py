import streamlit as st
import pandas as pd
from database import get_transactions


st.title("📈 Reports")


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


if len(df) > 0:

    st.subheader("Client Wise Report")

    client_report = df.groupby(
        "Client"
    )["Quantity"].sum()

    st.bar_chart(client_report)


    st.subheader("Employee Wise Report")

    employee_report = df.groupby(
        "Employee"
    )["Quantity"].sum()

    st.line_chart(employee_report)

else:

    st.info("No transactions available")
