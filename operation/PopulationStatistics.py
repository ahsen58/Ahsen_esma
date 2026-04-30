class PopulationStatistics:
    # Sınıf başlarken nüfus listesini (DTO listesi) içine alıyor
    def __init__(self, population_data_list):
        self.data = population_data_list
        self.toplam_kisi = len(self.data)

    def calculate_gender_percentages(self):
        # Eğer sistemde hiç kimse yoksa sıfıra bölünme (ZeroDivisionError) hatası almamak için kontrol
        if self.toplam_kisi == 0:
            return {"Kadın": 0.0, "Erkek": 0.0, "Diğer": 0.0}

        kadin_sayisi = 0
        erkek_sayisi = 0
        diger_sayisi = 0

        # Listedeki her bir kişiyi (DTO nesnesini) tek tek dönüyoruz
        for kisi in self.data:
            if kisi.gender == "Kadın":
                kadin_sayisi += 1
            elif kisi.gender == "Erkek":
                erkek_sayisi += 1
            else:
                diger_sayisi += 1

        # Yüzde Hesaplama Formülü: (İstenen Sayı / Toplam Sayı) * 100
        # round(deger, 2) metodu ile virgülden sonra sadece 2 basamak gösteriyoruz dmk
        kadin_yuzdesi = round((kadin_sayisi / self.toplam_kisi) * 100, 2)
        erkek_yuzdesi = round((erkek_sayisi / self.toplam_kisi) * 100, 2)

        # Sonuçları bir sözlük (dictionary) olarak döndürüyoruz
        return {
            "Kadın": kadin_yuzdesi,
            "Erkek": erkek_yuzdesi
        }

    def print_statistics_report(self):
        # Sadece ekrana şık bir çıktı vermek için yardımcı bir metod
        oranlar = self.calculate_gender_percentages()
        print("-" * 30)
        print("📊 NÜFUS CİNSİYET İSTATİSTİKLERİ")
        print("-" * 30)
        print(f"Toplam Nüfus : {self.toplam_kisi} kişi")
        print(f"Kadın Oranı  : %{oranlar['Kadın']}")
        print(f"Erkek Oranı  : %{oranlar['Erkek']}")
        print("-" * 30)