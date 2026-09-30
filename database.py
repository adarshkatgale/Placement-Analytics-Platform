import os
import sqlite3

os.makedirs("database", exist_ok=True)
# Here above commaned import SQLite3 in python
connection = sqlite3.connect('database/placement.db')
# here we are conecting the program with database
cursor= connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
    Student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Roll_no TEXT UNIQUE NOT NULL,
    Name TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    Branch TEXT NOT NULL,
    Tenth_percentage REAL NOT NULL,
    Twelfth_percentage REAL NOT NULL,
    CGPA REAL NOT NULL,
    Active_backlogs INTEGER NOT NULL,
    Graduation_year INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Companies(
    Company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Company_name TEXT NOT NULL,
    Minimum_cgpa REAL NOT NULL,
    Maximum_backlogs_allowed INTEGER NOT NULL,
    Graduation_year INTEGER NOT NULL,
    Minimum_tenth_percentage REAL NOT NULL,
    Minimum_twelfth_percentage REAL NOT NULL)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Company_Branches(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Company_id INTEGER,
    Branch TEXT NOT NULL,
    FOREIGN KEY (Company_id) REFERENCES Companies(Company_id)
)
""")

connection.commit()
