import streamlit as st
import pandas as pd
from database import get_transactions, delete_transaction
from io import BytesIO

st.title("📋 View Transactions")

data = get_transactions()

if data:

    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Item",
            "Quantity",
            "From Location",
            "Client",
            "Employee",
            "Date",
            "Status",
            "Remarks"
        ]
    )

    # Search
    search = st.text_input("🔍 Search Item")

    if search:
        df = df[
            df["Item"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    # Convert Date
    df["Date"] = pd.to_datetime(df["Date"])

    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input("From Date")

    with col2:
        end_date = st.date_input("To Date")

    df = df[
        (df["Date"] >= pd.to_datetime(start_date))
        &
        (df["Date"] <= pd.to_datetime(end_date))
    ]

    st.dataframe(
        df,
        use_container_width=True
    )

    # Excel Download
    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Transactions"
        )

    excel_data = output.getvalue()

    st.download_button(
        label="📥 Download Excel",
        data=excel_data,
        file_name="transactions.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    st.divider()

    st.subheader("Delete Transaction")

    delete_id = st.number_input(
    "Transaction ID",
    min_value=1,
    step=1,
    format="%d"
    )

    if st.button("Delete"):
    delete_transaction(int(delete_id))
    st.success("Transaction Deleted")
    st.rerun()

else:

    st.info("No Transactions Found")
