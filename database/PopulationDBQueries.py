import sqlite3

class PopulationDBQueries:
    def __init__(self, db_name="nufus_takip.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_population_table(self):
        # country, city ve district id'lerini Foreign Key (Yabancı Anahtar) mantığıyla tutuyoruz
        # is_working ve is_student için INTEGER kullanıyoruz (1 = Evet, 0 = Hayır)
        query = """
        CREATE TABLE IF NOT EXISTS Population (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country_id INTEGER NOT NULL,
            city_id INTEGER NOT NULL,
            district_id INTEGER NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            is_working INTEGER NOT NULL,
            is_student INTEGER NOT NULL
        )
        """
        self.cursor.execute(query)
        self.connection.commit()
        print("Population tablosu başarıyla oluşturuldu.")

    def insert_population(self, country_id, city_id, district_id, age, gender, is_working, is_student):
        query = """
        INSERT INTO Population (country_id, city_id, district_id, age, gender, is_working, is_student) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(query, (country_id, city_id, district_id, age, gender, is_working, is_student))
        self.connection.commit()
        print(f"Başarılı: Yeni nüfus kaydı eklendi! (Yaş: {age}, Cinsiyet: {gender})")

    def get_all_population(self):
        query = "SELECT * FROM Population"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()