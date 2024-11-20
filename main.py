import sqlite3

# connect to the database birthdays
def print_database():
    conn = sqlite3.connect('birthday_database.db')
    c = conn.cursor()

# Retrieve all birthdays    
    c.execute("SELECT * FROM birthdays")
    rows = c.fetchall()

# Print the birthdays
    for row in rows:
        print(row)

# Close the connection
    conn.close()

