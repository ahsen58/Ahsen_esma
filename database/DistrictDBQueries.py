import sqlite3

class DistrictDBQueries:
    def __init__(self, db_name="nufus_takip.db"):
        # Aynı veritabanı dosyasına bağlanıyoruz ki hepsi bir arada dursun
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_district_table(self):
        # city_id kolonunu ekleyerek ilçeyi şehre bağlıyoruz
        query = """
        CREATE TABLE IF NOT EXISTS District (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            code TEXT NOT NULL
        )
        """
        self.cursor.execute(query)
        self.connection.commit()
        print("District tablosu başarıyla oluşturuldu.")

    def insert_district(self, city_id, name, code):
        query = "INSERT INTO District (city_id, name, code) VALUES (?, ?, ?)"
        self.cursor.execute(query, (city_id, name, code))
        self.connection.commit()
        print(f"Başarılı: Şehir ID {city_id} olan {name} ({code}) District tablosuna eklendi!")

    def get_all_districts(self):
        query = "SELECT * FROM District"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_districts_by_city(self, city_id):
        # Sadece belirli bir şehre ait ilçeleri çekmek için metod
        query = "SELECT * FROM District WHERE city_id = ?"
        self.cursor.execute(query, (city_id,))
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()