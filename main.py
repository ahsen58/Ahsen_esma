import sqlite3

from database.CitiesDBQueries import CitiesDBQueries
from database.CountryDBQueries import CountryDBQueries
from database.DistrictDBQueries import DistrictDBQueries
from database.PopulationDBQueries import PopulationDBQueries
from dto.CityDTO import CityDTO
from dto.CountryDTO import CountryDTO
from dto.DistrictDTO import DistrictDTO

if __name__ == "__main__":
    db = DistrictDBQueries()
    ornek_ilceler = [
        ("Merkez", "MRK"),
        ("Kuzey", "KZY"),
        ("Güney", "GNY"),
        ("Doğu", "DGU"),
        ("Batı", "BTI"),
        ("Yeni", "YNI"),
        ("Eski", "ESK"),
        ("Tepe", "TPE"),
        ("Vadi", "VDI"),
        ("Ova", "OVA")
    ]

    for city_id in range(1, 101):

        # İç döngü: Her bir şehir ID'si için bu 10 ilçeyi dön
        for ilce_adi, ilce_kodu in ornek_ilceler:
            # İlçelerin hepsi "Merkez" olmasın diye başına Şehir ID'sini ekliyoruz
            # Örnek Çıktı: "Şehir 1 Merkez İlçesi", "Şehir 42 Doğu İlçesi" dmk
            ozel_ilce_adi = f"Şehir {city_id} {ilce_adi} İlçesi"

            # 1. DTO Nesnesini Yarat (district_id otomatik artacak, o yüzden None)
            yeni_ilce_dto = DistrictDTO(district_id=None, city_id=city_id, name=ozel_ilce_adi, code=ilce_kodu)

            # 2. Veritabanına Gönder
            db.insert_district(yeni_ilce_dto)

    db.close_connection()
