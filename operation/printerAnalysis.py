class ReportPrinter:
    def __init__(self, istatistik):
        self.ist = istatistik

    def print_report(self):
        print("-" * 35)
        print("NÜFUS İSTATİSTİK RAPORU")
        print("-" * 35)
        print(f"Toplam Nüfus  : {self.ist.toplam_kisi} kişi")
        oranlar = self.ist.gender.calculate()
        print(f"Kadın Oranı   : %{oranlar['Kadın']}")
        print(f"Erkek Oranı   : %{oranlar['Erkek']}")
        print(f"Ortalama Yaş  : {self.ist.age.average_age()}")
        print(f"Çalışan Oranı : %{self.ist.work.working_percentage()}")
        print(f"Öğrenci Oranı : %{self.ist.student.student_percentage()}")
        print("-" * 35)