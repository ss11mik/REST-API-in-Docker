# Script to initialize database file
#
# author: Ondrej Mikula
# 2023

import pysqlite3 as sqlite3
import os

os.remove("movies.db")
conn = sqlite3.connect("movies.db")

cursor = conn.cursor()
try:
    cursor.execute("""
        CREATE TABLE movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            release_year INTEGER
        ) STRICT;""")
    conn.commit()
except sqlite3.dbapi2.OperationalError:
    pass
