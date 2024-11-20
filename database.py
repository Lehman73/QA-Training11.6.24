import sqlite3

def create_user(name, month, day, family_database):
    conn = sqlite3.connect(f'{family_database}.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, month, day) VALUES (?, ?, ?)", (name, month, day)), (Melissa, May, 31)
    c.execute("INSERT INTO users (name, month, day) VALUES (?, ?, ?)", (name, month, day)), (Andrea, July, 3)
    c.execute("INSERT INTO users (name, month, day) VALUES (?, ?, ?)", (name, month, day)), (Dylan, November, 19)
    conn.commit()
    conn.close()

def update_user(name, month, day, family_database):
    conn = sqlite3.connect(f'{family_database}.db')
    c = conn.cursor()
    c.execute("UPDATE users SET month = ?, SET day = ? WHERE name = ?", (month, day, name))
    conn.commit()
    conn.close()

def delete_user(name, month, day, family_database):
    conn = sqlite3.connect(f'{family_database}.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, month, day) VALUES (?, ?, ?)", (name, month, day))
    conn.commit()
    conn.close()

def get_user(family_database):
    conn = sqlite3.connect(f'{family_database}.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, month, day) VALUES (?, ?, ?)", (name, month, day))
    conn.commit()
    conn.close()
    return User

def get_user_table(family_database):
    conn = sqlite3.connect(f'{family_database}.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users", ())
    all_users = c.fetchall()
    conn.close()
    return all_users

def print_database(family_database):
    conn = sqlite3.connect(f'{family_database}.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    for row in rows:
        print(row)

def create_database(family_database):
    # Create a connection to the database (If it doesn't exist, it will be created)
    conn = sqlite3.connect(f'{family_database}.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        name TEXT(15),
        month TEXT(10),
        day INTEGER(2)
    )''')
    conn.commit()
    conn.close()

    print("SQLite database named {family_database} created successfully!". 
    format(family_database))

