import sqlite3

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sys_command (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    command TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS web_command (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    command TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT
)
""")

conn.commit()
conn.close()

print("Tables created successfully")