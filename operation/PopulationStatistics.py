class PopulationStatistics:
    # Sınıf başlarken nüfus listesini (DTO listesi) içine alıyor
    def __init__(self, population_data_list):
        self.data = population_data_list
        self.toplam_kisi = len(self.data)

    def calculate_gender_percentages(self):
        if self.toplam_kisi == 0:
            return {"Kadın": 0.0, "Erkek": 0.0, "Diğer": 0.0}

        kadin_sayisi = 0
        erkek_sayisi = 0
        diger_sayisi = 0


        for kisi in self.data:
            if kisi.gender == "Kadın":
                kadin_sayisi += 1
            elif kisi.gender == "Erkek":
                erkek_sayisi += 1
            else:
                diger_sayisi += 1


        kadin_yuzdesi = round((kadin_sayisi / self.toplam_kisi) * 100, 2)
        erkek_yuzdesi = round((erkek_sayisi / self.toplam_kisi) * 100, 2)


        return {
            "Kadın": kadin_yuzdesi,
            "Erkek": erkek_yuzdesi
        }

    def print_statistics_report(self):
        oranlar = self.calculate_gender_percentages()
        print("-" * 30)
        print("📊 NÜFUS CİNSİYET İSTATİSTİKLERİ")
        print("-" * 30)
        print(f"Toplam Nüfus : {self.toplam_kisi} kişi")
        print(f"Kadın Oranı  : %{oranlar['Kadın']}")
        print(f"Erkek Oranı  : %{oranlar['Erkek']}")
        print("-" * 30)