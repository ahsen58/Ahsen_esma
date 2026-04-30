
import sqlite3

from database.DBQueries import DBQueries

if __name__ == "__main__":
    db = DBQueries()
    db.insert_country("Türkiye","90")
    db.close_connection()