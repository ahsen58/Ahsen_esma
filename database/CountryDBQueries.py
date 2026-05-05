import sqlite3

from dto.CountryDTO import CountryDTO


class CountryDBQueries:
    def __init__(self, db_name="nufus_takip.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_country_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS Country (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            code TEXT NOT NULL
        )
        """
        self.cursor.execute(query)
        self.connection.commit()

    def insert_country(self, country:CountryDTO):
        query = "INSERT INTO Country (name, code) VALUES (?, ?)"
        self.cursor.execute(query, (country.name, country.code))
        self.connection.commit()
        print(f"Başarılı: {country.name} ({country.code}) tablolaya eklendi!")

    def get_all_countries(self):
        query = "SELECT * FROM Country"
        self.cursor.execute(query)
        countries = self.cursor.fetchall()

        country_dto_list = []

        for row in countries:
            dto = CountryDTO(row[0], row[1], row[2])
            country_dto_list.append(dto)
        return country_dto_list

    def delete_all_countries(self):
        query = "DELETE FROM Country"
        self.cursor.execute(query)
        reset_query = "DELETE FROM sqlite_sequence WHERE name='Country'"
        self.cursor.execute(reset_query)
        self.connection.commit()
        print("Başarılı: Tüm ülkeler silindi ve ID sayacı sıfırlandı!")
    def close_connection(self):
        self.connection.close()