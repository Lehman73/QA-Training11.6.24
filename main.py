import sqlite3

# connect to the database family
def print_database():
    conn = sqlite3.connect('family_database.db')
    c = conn.cursor()

# Retrieve all users   
    c.execute("SELECT * FROM users")
    rows = c.fetchall()

# Print the users
    for row in rows:
        print(row)

# Close the connection
    conn.close()

