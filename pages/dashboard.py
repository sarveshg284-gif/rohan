import streamlit as st
import pandas as pd
from database.database import get_transactions


# Page configuration
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Office Transaction Dashboard")


# Refresh button
if st.button("🔄 Refresh Dashboard"):
    st.rerun()


# Get transaction data from database
df = get_transactions()


# Check data availability
if df.empty:

    st.warning(
        "No transactions found. Please add transactions first."
    )

else:

    # ---------------- KPI CARDS ----------------

    total_transactions = len(df)

    total_quantity = df["quantity"].sum()

    pending = len(
        df[df["status"] == "Pending"]
    )

    delivered = len(
        df[df["status"] == "Delivered"]
    )

    in_transit = len(
        df[df["status"] == "In Transit"]
    )


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "📋 Total Transactions",
        total_transactions
    )


    col2.metric(
        "📦 Total Quantity",
        total_quantity
    )


    col3.metric(
        "⏳ Pending",
        pending
    )


    col4.metric(
        "✅ Delivered",
        delivered
    )


    st.divider()


    # ---------------- STATUS CHART ----------------

    st.subheader(
        "📈 Transaction Status"
    )


    status_count = (
        df["status"]
        .value_counts()
    )


    st.bar_chart(
        status_count
    )


    st.divider()


    # ---------------- CATEGORY CHART ----------------

    st.subheader(
        "📦 Category Wise Transactions"
    )


    category_count = (
        df["category"]
        .value_counts()
    )


    st.bar_chart(
        category_count
    )


    st.divider()


    # ---------------- RECENT TRANSACTIONS ----------------

    st.subheader(
        "📝 Recent Transactions"
    )


    recent = df.head(10)


    st.dataframe(
        recent,
        use_container_width=True
    )


    st.divider()


    # ---------------- CLIENT SUMMARY ----------------

    st.subheader(
        "🏢 Client Wise Transactions"
    )


    client_count = (
        df["to_client"]
        .value_counts()
    )


    st.bar_chart(
        client_count
    )
