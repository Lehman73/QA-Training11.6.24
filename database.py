import sqlite3


def create_user(Firstname, Lastname, Month, Day, Year, Age, birthday_database):
    conn = sqlite3.connect(f'{birthday_database}.db')
    c = conn.cursor()
    c.execute("INSERT INTO birthdays (Firstname, Lastname, Month, Day, Year, Age) VALUES (?, ?, ?, ?, ?, ?)", (Firstname, Lastname, Month, Day, Year, Age))
    c.execute("INSERT INTO birthdays (Firstname, Lastname, Month, Day, Year, Age) VALUES (?, ?, ?, ?, ?, ?)", ('Melissa','Lehman', 'May', '31', '1973', '51'))
    c.execute("INSERT INTO birthdays (Firstname, Lastname, Month, Day, Year, Age) VALUES (?, ?, ?, ?, ?, ?)", ('Andrea','Lehman', 'July', '03', '1998', '26'))
    conn.commit()
    conn.close()

def update_user(Firstname, Lastname, Month, Day, Year, Age, birthday_database):
    conn = sqlite3.connect(f'{birthday_database}.db')
    c = conn.cursor()
    c.execute("UPDATE birthdays SET age = ? WHERE Firstname = ? AND Lastname = ?", (age, firstname, Lastname))
    conn.commit()
    conn.close()

def delete_user(Firstname, Lastname, Month, Day, Year, Age, birthday_database):
    conn = sqlite3.connect(f'{birthday_database}.db')
    c = conn.cursor()
    c.execute("DELETE FROM birthdays WHERE firstname = ? AND lastname = ?", (Firstname, Lastname))
    conn.commit()
    conn.close()

def get_user(firstname, lastname, birthday_database):
    conn = sqlite3.connect(f'{birthday_database}.db')
    c = conn.cursor()
    c.execute("SELECT * FROM birthdays WHERE firstname = ? AND lastname = ?", (Firstname, Lastname))
    user = c.fetchone()
    conn.close()
    return user

def get_user_table(birthday_database):
    conn = sqlite3.connect(f'{birthday_database}.db')
    c = conn.cursor()
    c.execute("SELECT * FROM birthdays", ())
    all_users = c.fetchall()
    conn.close()
    return all_users

def delete_users_from_user_table(birthday_database):
    conn = sqlite3.connect(f'{birthday_database}.db')
    c = conn.cursor()
    c.execute("DELETE FROM birthdays")
    conn.commit()
    conn.close()

def print_database(birthday_database):
    conn = sqlite3.connect(f'{birthday_database}.db')
    c = conn.cursor()
    c.execute("SELECT * FROM birthdays")
    rows = c.fetchall()
    for row in rows:
        print(row)
def create_database(birthday_database):
    # Create a connection to the database (it will be created if it doesn't exist)
    conn = sqlite3.connect('{birthday_database}.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS table (
    Firstname TEXT(15),
    Lastname TEXT(15),
    Month TEXT(9),
    Day INTEGER(2),
    Year INTEGER(4),
    Age INTEGER(2)
                )''')
    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

print("SQLite3 database created successfully!")

