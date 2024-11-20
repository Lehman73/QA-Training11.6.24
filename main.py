import sqlite3

# connect to the database birthdays
conn = sqlite3.connect('birthday_database.db')
c = conn.cursor()

# Retrieve all birthdays
c.execute("SELECT * FROM birthdays")
birthdays = c.fetchall()

# Print the birthdays
for birthdays in birthdays:
    print(firstname, lastname, month, day, year, age)

# Close the connection
conn.close()

