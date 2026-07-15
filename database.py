import sqlite3


conn = sqlite3.connect(
    "transactions.db",
    check_same_thread=False
)

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
item TEXT,
quantity INTEGER,
from_location TEXT,
client  TEXT,
employee TEXT,
date TEXT,
status TEXT,
remarks TEXT
)
""")


conn.commit()



def add_transaction(
    item,
    quantity,
    from_location,
    client,
    employee,
    date,
    status,
    remarks
):

    cursor.execute(
        """
        INSERT INTO transactions
        (
        item,
        quantity,
        from_location,
        client,
        employee,
        date,
        status,
        remarks
        )
        VALUES (?,?,?,?,?,?,?,?)
        """,
        (
        item,
        quantity,
        from_location,
        client,
        employee,
        date,
        status,
        remarks
        )
    )

    conn.commit()



def get_transactions():

    cursor.execute(
        """
        SELECT *
        FROM transactions
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()



def delete_transaction(transaction_id):

    cursor.execute(
        """
        DELETE FROM transactions
        WHERE id=?
        """,
        (transaction_id,)
    )

    conn.commit()
