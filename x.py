
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    rollno INTEGER,
    email TEXT,
    contact INTEGER,
    branch TEXT
);''')
               
cursor.execute('''CREATE TABLE IF NOT EXISTS faculties(
    id INTEGER PRIMARY KEY,
    name TEXT,
    faculty_id INTEGER,
    email TEXT,
    phone_number INTEGER,
    qualifications TEXT
);''')
x=9898
y=989989
conn.commit()

conn.close()