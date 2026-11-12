"""
Codeunit: sqlite_db.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Database operations for file watching.
"""
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database_dir = os.path.join(BASE_DIR, 'db')
database_path = os.path.join(database_dir, 'filewatch.db')

os.makedirs(database_dir, exist_ok=True)


def initiate_database():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('''SELECT 1 + 1;''')
    selection = cursor.fetchall()
    return selection

def create_table():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS file_watch (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_path TEXT NOT NULL,
            pgp_key TEXT,
            cron_expression TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

def insert_file_watch_data(file_path, pgp_key, cron_expression):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO file_watch (file_path, pgp_key, cron_expression)
        VALUES (?, ?, ?);
    ''', (file_path, pgp_key, cron_expression))
    conn.commit()
    conn.close()

def retrieve_file_watch_data():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM file_watch;')
    data = cursor.fetchall()
    conn.close()
    return data
