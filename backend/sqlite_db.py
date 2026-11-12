"""
Codeunit: sqlite_db.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Database operations for file watching.
"""
import sqlite3


def initiate_database():
    conn = sqlite3.connect('filewatch.db')
    return conn
