import sqlite3

from dto.DistrictDTO import DistrictDTO


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

    def insert_district(self, district:DistrictDTO):
        query = "INSERT INTO District (city_id, name, code) VALUES (?, ?, ?)"
        self.cursor.execute(query, (district.city_id, district.name,district.code))
        self.connection.commit()
        print(f"Başarılı: Şehir ID {district.city_id} olan {district.name} ({district.code}) District tablosuna eklendi!")

    def get_all_districts(self):
        query = "SELECT * FROM District"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_districts_by_city(self, city_id):
        # Sadece belirli bir şehre ait ilçeleri çekmek için metod
        query = "SELECT * FROM District WHERE city_id = ?"
        self.cursor.execute(query, (city_id,))
        rows = self.cursor.fetchall()  # Ham veriyi çekiyoruz

        district_dto_list = []  # DTO'ları koyacağımız boş liste

        # AYNI FOR DÖNGÜSÜ BURADA DA VAR
        for row in rows:
            dto = DistrictDTO(district_id=row[0], city_id=row[1], name=row[2], code=row[3])
            district_dto_list.append(dto)

        return district_dto_list  # Seçilen şehre ait ilçelerin DTO listesi dönüyor
    def close_connection(self):
        self.connection.close()