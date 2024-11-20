import sqlite3

# connect to the database Family
def print_database():
    conn = sqlite3.connect('family_database.db')
    c = conn.cursor()

# Retrieve all Family   
    c.execute("SELECT * FROM Family")
    rows = c.fetchall()

# Print the Family
    for row in rows:
        print(row)

# Close the connection
    conn.close()

