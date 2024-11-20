import database

def print_mydatabase():

    # Create a connection to the database (it will be created if it doesn't exist)
    Connection = sqlite3.connect('family_database.db')

    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()

    # Create a Table (if it doesn't exist)
    Cursor.execute ('''CREATE a Table IF NOT EXISTS users (name, month, day)''')
    
    # Commit the changes
    connection.commit()

    # Close the connection
    connection.close()

    print ("SQLite3 database created successfully!")
