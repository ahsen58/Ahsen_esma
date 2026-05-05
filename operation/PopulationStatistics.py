class PopulationStatistics:
    def __init__(self, population_data_list):
        self.data = population_data_list
        self.toplam_kisi = len(self.data)

    def calculate_gender_percentages(self):
        if self.toplam_kisi == 0:
            return {"Kadın": 0.0, "Erkek": 0.0, "Diğer": 0.0}
        kadin = sum(1 for k in self.data if k.gender == "Kadın")
        erkek = sum(1 for k in self.data if k.gender == "Erkek")
        diger = self.toplam_kisi - kadin - erkek
        return {
            "Kadın": round((kadin / self.toplam_kisi) * 100, 2),
            "Erkek": round((erkek / self.toplam_kisi) * 100, 2),
            "Diğer": round((diger / self.toplam_kisi) * 100, 2)
        }

    def calculate_average_age(self):
        if self.toplam_kisi == 0:
            return 0.0
        return round(sum(k.age for k in self.data) / self.toplam_kisi, 1)

    def calculate_working_percentage(self):
        if self.toplam_kisi == 0:
            return 0.0
        calisan = sum(1 for k in self.data if k.is_working == 1)
        return round((calisan / self.toplam_kisi) * 100, 2)

    def calculate_student_percentage(self):
        if self.toplam_kisi == 0:
            return 0.0
        ogrenci = sum(1 for k in self.data if k.is_student == 1)
        return round((ogrenci / self.toplam_kisi) * 100, 2)

    def get_age_groups(self):
        gruplar = {"0-17": 0, "18-35": 0, "36-60": 0, "60+": 0}
        for k in self.data:
            if k.age < 18:
                gruplar["0-17"] += 1
            elif k.age <= 35:
                gruplar["18-35"] += 1
            elif k.age <= 60:
                gruplar["36-60"] += 1
            else:
                gruplar["60+"] += 1
        return gruplar

    def get_min_max_age(self):
        if self.toplam_kisi == 0:
            return {"En Genç": 0, "En Yaşlı": 0}
        return {
            "En Genç": min(k.age for k in self.data),
            "En Yaşlı": max(k.age for k in self.data)
        }

    def print_statistics_report(self):
        oranlar = self.calculate_gender_percentages()
        print("-" * 35)
        print("NÜFUS İSTATİSTİK RAPORU")
        print("-" * 35)
        print(f"Toplam Nüfus  : {self.toplam_kisi} kişi")
        print(f"Kadın Oranı   : %{oranlar['Kadın']}")
        print(f"Erkek Oranı   : %{oranlar['Erkek']}")
        print(f"Ortalama Yaş  : {self.calculate_average_age()}")
        print(f"Çalışan Oranı : %{self.calculate_working_percentage()}")
        print(f"Öğrenci Oranı : %{self.calculate_student_percentage()}")
        print("-" * 35)
