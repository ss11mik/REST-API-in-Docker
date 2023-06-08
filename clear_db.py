# Script to empty the database file
#
# author: Ondrej Mikula
# 2023

import pysqlite3 as sqlite3

conn = sqlite3.connect("movies.db")

cursor = conn.cursor()
try:
    cursor.execute("DELETE FROM movies;")
    conn.commit()
except sqlite3.dbapi2.OperationalError:
    print("aaa")
    pass
