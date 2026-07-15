if submit:

    try:

        add_transaction(
            description,
            category,
            quantity,
            from_location,
            client,
            employee,
            "",
            str(transaction_date),
            status,
            remark
        )

        st.success(
            "Transaction Saved Successfully"
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )
