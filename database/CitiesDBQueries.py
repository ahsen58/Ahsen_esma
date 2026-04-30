import sqlite3

class CitiesDBQueries:
    # db_name aynı kalmalı ki Country tablosuyla aynı dosyanın içine yazılsın
    def __init__(self, db_name="nufus_takip.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_city_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS City (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            code TEXT NOT NULL
        )
        """
        self.cursor.execute(query)
        self.connection.commit()
        print("City tablosu başarıyla oluşturuldu.")

    def insert_city(self,country_id, name, code):
        query = "INSERT INTO City (country_id,name, code) VALUES (?,?, ?)"
        self.cursor.execute(query, (country_id,name, code))
        self.connection.commit()
        print(f"Başarılı: {country_id} {name} ({code}) City tablosuna eklendi!")

    def get_cities_from_country_id(self,country_id):
        query = "SELECT * FROM City where country_id = ?"
        self.cursor.execute(query, (country_id,))
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()