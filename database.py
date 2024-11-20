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
    
def get_user(name, month, day, family_database):
    conn = sqlite3.connect(f'{family_database}.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, month, day) VALUES (?, ?, ?)", (name, month, day))
    conn.commit()
    conn.close()