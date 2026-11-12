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
