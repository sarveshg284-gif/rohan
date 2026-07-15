import sqlite3
import pandas as pd

conn = sqlite3.connect("database/transaction.db", check_same_thread=False)
cursor = conn.cursor()



# ---------------- TRANSACTIONS ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    quantity INTEGER,
    from_location TEXT,
    to_client TEXT,
    employee TEXT,
    date TEXT,
    status TEXT,
    remarks TEXT
)
""")

conn.commit()


# ================= TRANSACTIONS =================

def add_transaction(
    category,
    quantity,
    from_location,
    to_client,
    employee,
    date,
    status,
    remarks,
):
    cursor.execute(
        """
        INSERT INTO transactions(
            category,
            quantity,
            from_location,
            to_client,
            employee,
            date,
            status,
            remarks
        )
        VALUES(?,?,?,?,?,?,?,?,?,?)
        """,
        (
            category,
            quantity,
            from_location,
            to_client,
            employee,
            date,
            status,
            remarks,
        ),
    )

    conn.commit()

def get_today_transactions(date):
    return pd.read_sql(
        f"SELECT * FROM transactions WHERE date='{date}'",
        conn
    )
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
