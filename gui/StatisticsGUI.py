import tkinter as tk
from tkinter import ttk, messagebox
from database.CitiesDBQueries import CitiesDBQueries
from database.CountryDBQueries import CountryDBQueries
from database.DistrictDBQueries import DistrictDBQueries
from database.PopulationDBQueries import PopulationDBQueries
from gui.LocationSelectorFrame import LocationSelectorFrame
from operation.PopulationStatistics import PopulationStatistics

class StatisticsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bölgesel İstatistik Raporu")
        self.root.geometry("450x550")
        self.country_db = CountryDBQueries()
        self.city_db = CitiesDBQueries()
        self.district_db = DistrictDBQueries()
        self.pop_db = PopulationDBQueries()
        self.arayuzu_olustur()

    def arayuzu_olustur(self):
        self.location_selector = LocationSelectorFrame(
            self.root, self.country_db, self.city_db, self.district_db
        )
        self.location_selector.pack(pady=15)

        btn_hesapla = ttk.Button(self.root, text="İstatistikleri Getir", command=self.istatistik_hesapla)
        btn_hesapla.pack(pady=10, ipady=5, ipadx=10)

        self.result_frame = ttk.LabelFrame(self.root, text=" Analiz Sonuçları ")
        self.result_frame.pack(pady=15, padx=30, fill="both", expand=True)

        self.lbl_toplam = ttk.Label(self.result_frame, text="Toplam Nüfus: -", font=("Helvetica", 12, "bold"))
        self.lbl_toplam.pack(pady=8)

        self.lbl_kadin = ttk.Label(self.result_frame, text="Kadın Oranı: -", font=("Helvetica", 11))
        self.lbl_kadin.pack(pady=5)

        self.lbl_erkek = ttk.Label(self.result_frame, text="Erkek Oranı: -", font=("Helvetica", 11))
        self.lbl_erkek.pack(pady=5)

        self.lbl_ort_yas = ttk.Label(self.result_frame, text="Ortalama Yaş: -", font=("Helvetica", 11))
        self.lbl_ort_yas.pack(pady=5)

        self.lbl_calisan = ttk.Label(self.result_frame, text="Çalışan Oranı: -", font=("Helvetica", 11))
        self.lbl_calisan.pack(pady=5)

        self.lbl_ogrenci = ttk.Label(self.result_frame, text="Öğrenci Oranı: -", font=("Helvetica", 11))
        self.lbl_ogrenci.pack(pady=5)

    def istatistik_hesapla(self):
        selected_ids = self.location_selector.get_selected_ids()
        if selected_ids is None:
            messagebox.showwarning("Eksik Seçim", "Lütfen Ülke, Şehir ve İlçe seçimlerini eksiksiz yapın.")
            return

        c_id, city_id, dist_id = selected_ids
        ilce_nufusu_listesi = self.pop_db.get_population_by_district(dist_id)

        if len(ilce_nufusu_listesi) == 0:
            messagebox.showinfo("Bilgi", "Seçilen ilçede henüz kayıtlı nüfus bulunmamaktadır.")
            self.lbl_toplam.config(text="Toplam Nüfus: 0")
            self.lbl_kadin.config(text="Kadın Oranı: %0")
            self.lbl_erkek.config(text="Erkek Oranı: %0")
            self.lbl_ort_yas.config(text="Ortalama Yaş: -")
            self.lbl_calisan.config(text="Çalışan Oranı: %0")
            self.lbl_ogrenci.config(text="Öğrenci Oranı: %0")
            return

        uzman = PopulationStatistics(ilce_nufusu_listesi)
        oranlar = uzman.calculate_gender_percentages()

        self.lbl_toplam.config(text=f"Toplam Nüfus: {uzman.toplam_kisi} Kişi")
        self.lbl_kadin.config(text=f"Kadın Oranı: %{oranlar['Kadın']}")
        self.lbl_erkek.config(text=f"Erkek Oranı: %{oranlar['Erkek']}")
        self.lbl_ort_yas.config(text=f"Ortalama Yaş: {uzman.calculate_average_age()}")
        self.lbl_calisan.config(text=f"Çalışan Oranı: %{uzman.calculate_working_percentage()}")
        self.lbl_ogrenci.config(text=f"Öğrenci Oranı: %{uzman.calculate_student_percentage()}")
