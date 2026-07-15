import sqlite3
import pandas as pd

conn = sqlite3.connect("database/transaction.db", check_same_thread=False)
cursor = conn.cursor()

# ---------------- USERS ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

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


# ===================== USERS =====================

def add_user(fullname, username, password, role):
    cursor.execute(
        """
        INSERT INTO users(fullname, username, password, role)
        VALUES(?,?,?,?)
        """,
        (fullname, username, password, role),
    )
    conn.commit()


def get_users():
    return pd.read_sql("SELECT * FROM users", conn)


def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
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
