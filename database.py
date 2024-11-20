import sqlite3


def create_Family(Firstname, Lastname, Month, Day, family_database):
    conn = sqlite3.connect(f'{family_database}.db')
    c = conn.cursor()
    c.execute("INSERT INTO Family (Firstname, Lastname, Month, Day) VALUES (?, ?, ?, ?)", (Melissa, Lehman, May, 31))
    c.execute("INSERT INTO Family (Firstname, Lastname, Month, Day) VALUES (?, ?, ?, ?)", (Andrea, Penny, July, 3))
    conn.commit()
    conn.close()

def update_Family(Firstname, Lastname, Month, Day, family_database):
    conn = sqlite3.connect(f'{family_database}.db')
    c = conn.cursor()
    c.execute("UPDATE Family SET Month = ? AND SET Day = ? WHERE Firstname = ? AND WHERE Lastname = ?", (Month, Day, Firstname, Lastname))
    conn.commit()
    conn.close()

def delete_Family(Firstname, Lastname, Month, Day, family_database):
    conn = sqlite3.connect(f'{family_database}.db')
    c = conn.cursor()
    c.execute("DELETE FROM Family WHERE firstname = ? AND WHERE lastname = ?", (Firstname, Lastname, Month, Day))
    conn.commit()
    conn.close()

def get_Family(firstname, lastname, Month, Day, family_database):
    conn = sqlite3.connect(f'{family_database}.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Family WHERE firstname = ? AND lastname = ?", (Firstname, Lastname, Month, Day))
    user = c.fetchone()
    conn.close()
    return Family 

def get_Family_table(family_database):
    conn = sqlite3.connect(f'{family_database}.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Family", ())
    all_Family = c.fetchall()
    conn.close()
    return all_Family

def delete_Family_from_Family_table(family_database):
    conn = sqlite3.connect(f'{family_database}.db')
    c = conn.cursor()
    c.execute("DELETE FROM Family")
    conn.commit()
    conn.close()

def print_database(family_database):
    conn = sqlite3.connect(f'{family_database}.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Family")
    rows = c.fetchall()
    for row in rows:
        print(row)
def create_database(family_database):
    # Create a connection to the database (it will be created if it doesn't exist)
    conn = sqlite3.connect('{family_database}.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Family (
    Firstname TEXT(15),
    Lastname TEXT(15),
    Month TEXT(9),
    Day INTEGER(2)
    )''')

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

print("SQLite3 database created successfully!")

