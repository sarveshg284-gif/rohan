import sqlite3

conn = sqlite3.connect(
    "transactions.db",
    check_same_thread=False
)

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE,
password TEXT,
role TEXT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
id INTEGER PRIMARY KEY AUTOINCREMENT,
item TEXT,
quantity INTEGER,
from_location TEXT,
client TEXT,
employee TEXT,
date TEXT,
remarks TEXT
)
""")


cursor.execute("""
INSERT OR IGNORE INTO users
(username,password,role)
VALUES
('admin','admin123','Admin'),
('staff','staff123','Staff')
""")


conn.commit()



def login(username,password):

    cursor.execute(
        """
        SELECT * FROM users
        WHERE username=? AND password=?
        """,
        (username,password)
    )

    return cursor.fetchone()



def add_transaction(
    item,
    quantity,
    from_location,
    client,
    employee,
    date,
    remarks
):

    cursor.execute(
        """
        INSERT INTO transactions
        VALUES(
        NULL,?,?,?,?,?,?,?
        )
        """,
        (
            item,
            quantity,
            from_location,
            client,
            employee,
            date,
            remarks
        )
    )

    conn.commit()



def get_transactions():

    cursor.execute(
        """
        SELECT * FROM transactions
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()



def delete_transaction(id):

    cursor.execute(
        "DELETE FROM transactions WHERE id=?",
        (id,)
    )

    conn.commit()
