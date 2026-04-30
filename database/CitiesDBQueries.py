import sqlite3

from dto.CityDTO import CityDTO

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

    def insert_city(self,city:CityDTO):
        query = "INSERT INTO City (country_id,name, code) VALUES (?,?, ?)"
        self.cursor.execute(query, (city.country_id,city.name, city.code))
        self.connection.commit()
        print(f"Başarılı: {city.country_id} {city.name} ({city.code}) City tablosuna eklendi!")

    def get_cities_from_country_id(self,country_id):
        query = "SELECT * FROM City where country_id = ?"
        self.cursor.execute(query, (country_id,))
        rows = self.cursor.fetchall()
        city_dto_list = []  # Objelerimizi koyacağımız boş sepet

        for row in rows:
            # row[0]=id, row[1]=country_id, row[2]=name, row[3]=code
            # Ham veriyi alıp CityDTO objesine döküyoruz
            dto = CityDTO(row[0], row[1], row[2], row[3])

            # Oluşan objeyi sepete ekliyoruz
            city_dto_list.append(dto)

        return city_dto_list

    def delete_all_cities(self):
        # 1. Tablodaki tüm verileri siler
        query = "DELETE FROM City"
        self.cursor.execute(query)

        # 2. AUTOINCREMENT (otomatik artan ID) sayacını sıfırlar
        # Böylece yeni veri eklendiğinde ID tekrar 1'den başlar
        reset_query = "DELETE FROM sqlite_sequence WHERE name='City'"
        self.cursor.execute(reset_query)

        self.connection.commit()
        print("Başarılı: Tüm şehirler silindi ve ID sayacı sıfırlandı!")

    def close_connection(self):
        self.connection.close()