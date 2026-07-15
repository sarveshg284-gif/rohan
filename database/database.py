import sqlite3
import pandas as pd

conn = sqlite3.connect("database/transaction.db", check_same_thread=False)
cursor = conn.cursor()



# ---------------- TRANSACTIONS ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    category TEXT,
    quantity INTEGER,
    from_location TEXT,
    to_client TEXT,
    employee TEXT,
    vehicle TEXT,
    date TEXT,
    status TEXT,
    remarks TEXT
)
""")

conn.commit()


# ================= TRANSACTIONS =================

def add_transaction(
    description,
    category,
    quantity,
    from_location,
    to_client,
    employee,
    vehicle,
    date,
    status,
    remarks,
):
    cursor.execute(
        """
        INSERT INTO transactions(
            description,
            category,
            quantity,
            from_location,
            to_client,
            employee,
            vehicle,
            date,
            status,
            remarks
        )
        VALUES(?,?,?,?,?,?,?,?,?,?)
        """,
        (
            description,
            category,
            quantity,
            from_location,
            to_client,
            employee,
            vehicle,
            date,
            status,
            remarks,
        ),
    )

    conn.commit()


def get_transactions():
    return pd.read_sql(
        "SELECT * FROM transactions ORDER BY id DESC",
        conn,
    )


def delete_transaction(transaction_id):
    cursor.execute(
        "DELETE FROM transactions WHERE id=?",
        (transaction_id,),
    )
    conn.commit()
