import streamlit as st
import pandas as pd
from database.database import get_transactions


st.title("📊 Dashboard")


# Get data from database
df = get_transactions()


if df.empty:

    st.warning("No transactions found")

else:

    # Calculate statistics

    total_transactions = len(df)

    pending = len(
        df[df["status"] == "Pending"]
    )

    delivered = len(
        df[df["status"] == "Delivered"]
    )

    in_transit = len(
        df[df["status"] == "In Transit"]
    )


    # Display cards

    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "Total Transactions",
        total_transactions
    )

    col2.metric(
        "Pending",
        pending
    )

    col3.metric(
        "Delivered",
        delivered
    )

    col4.metric(
        "In Transit",
        in_transit
    )


    st.divider()


    # Transaction chart

    st.subheader("📈 Transaction Status")


    status_count = df["status"].value_counts()


    st.bar_chart(status_count)


    st.divider()


    # Category chart

    st.subheader("📦 Category Wise Transactions")


    category_count = df["category"].value_counts()


    st.bar_chart(category_count)


    st.divider()


    # Recent transactions

    st.subheader("Recent Transactions")


    st.dataframe(
        df.head(10),
        use_container_width=True
    )
