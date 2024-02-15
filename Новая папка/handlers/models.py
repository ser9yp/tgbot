import sqlite3

def get_all_vectors(vector_name):
    connection = sqlite3.connect("./sqlite/db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM vectors")

    return cursor.fetchall