import sqlite3

class DataBaseCreator:
    def __init__(self, db_name="nufus_takip.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        print(f"'{db_name}' başarıyla oluşturuldu ve bağlanıldı!")

    def close_connection(self):
        self.connection.close()
        print("Veritabanı bağlantısı kapatıldı.")