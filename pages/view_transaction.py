import streamlit as st
import pandas as pd
from database.database import get_transactions, delete_transaction


st.title("📋 Transactions")


# Get transactions from database
df = get_transactions()


if df.empty:

    st.info("No transactions available")

else:

    # Search box
    search = st.text_input(
        "🔍 Search Description / Client"
    )


    # Status filter
    status = st.selectbox(
        "Filter Status",
        [
            "All",
            "Pending",
            "In Transit",
            "Delivered"
        ]
    )


    # Search filtering
    if search:

        df = df[
            df["description"]
            .str.contains(
                search,
                case=False,
                na=False
            )
            |
            df["to_client"]
            .str.contains(
                search,
                case=False,
                na=False
            )
        ]


    # Status filtering
    if status != "All":

        df = df[
            df["status"] == status
        ]


    # Display table

    st.subheader("Transaction List")

    st.dataframe(
        df,
        use_container_width=True
    )


    # Delete transaction

    st.divider()

    st.subheader("🗑 Delete Transaction")


    transaction_id = st.number_input(
        "Enter Transaction ID",
        min_value=1,
        step=1
    )


    if st.button("Delete"):

        delete_transaction(
            transaction_id
        )

        st.success(
            "Transaction deleted successfully"
        )

        st.rerun()
