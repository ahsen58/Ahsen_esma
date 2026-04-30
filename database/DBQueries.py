import sqlite3


class DBQueries:
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

    def insert_country(self, name, code):
        # ? işaretleri güvenlik için kullanılır (SQL Injection'ı önler)
        query = "INSERT INTO Country (name, code) VALUES (?, ?)"

        # ? olan yerlere sırasıyla name ve code değişkenleri yerleşir
        self.cursor.execute(query, (name, code))
        self.connection.commit()  # Veriyi kalıcı olarak kaydeder
        print(f"Başarılı: {name} ({code}) tablolaya eklendi!")

    def close_connection(self):
        self.connection.close()