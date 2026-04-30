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
        # ? işaretleri güvenlik için kullanılır (SQL Injection'ı önler)
        query = "INSERT INTO Country (name, code) VALUES (?, ?)"

        # ? olan yerlere sırasıyla name ve code değişkenleri yerleşir
        self.cursor.execute(query, (country.name, country.code))
        self.connection.commit()  # Veriyi kalıcı olarak kaydeder
        print(f"Başarılı: {country.name} ({country.code}) tablolaya eklendi!")

    def get_all_countries(self):
        query = "SELECT * FROM Country"
        self.cursor.execute(query)

        # fetchall() tablodaki tüm satırları bir liste olarak alır
        # Örnek Çıktı: [(1, 'Türkiye', 'TR'), (2, 'Almanya', 'DE')]
        countries = self.cursor.fetchall()

        country_dto_list = []

        for row in countries:
            # row[0] = id, row[1] = name, row[2] = code
            # Her satır verisiyle yeni bir CountryDTO nesnesi yaratıp listeye ekliyoruz
            dto = CountryDTO(row[0], row[1], row[2])
            country_dto_list.append(dto)

        # Artık ham veri (tuple) değil, içi CountryDTO dolu listeyi döndürüyoruz
        return country_dto_list

    def delete_all_countries(self):
        # 1. Tablodaki tüm verileri siler
        query = "DELETE FROM Country"
        self.cursor.execute(query)

        # 2. AUTOINCREMENT (otomatik artan ID) sayacını sıfırlar
        # Böylece yeni veri eklendiğinde ID tekrar 1'den başlar
        reset_query = "DELETE FROM sqlite_sequence WHERE name='Country'"
        self.cursor.execute(reset_query)

        self.connection.commit()
        print("Başarılı: Tüm ülkeler silindi ve ID sayacı sıfırlandı!")

    def close_connection(self):
        self.connection.close()