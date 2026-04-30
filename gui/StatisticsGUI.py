import tkinter as tk
from tkinter import ttk, messagebox

from database.CitiesDBQueries import CitiesDBQueries
from database.CountryDBQueries import CountryDBQueries
from database.DistrictDBQueries import DistrictDBQueries
from database.PopulationDBQueries import PopulationDBQueries
from dto.CountryDTO import CountryDTO
from gui.LocationSelectorFrame import LocationSelectorFrame
from operation.PopulationStatistics import PopulationStatistics


# Kendi dosyalarından gerekli sınıfları import et
# from LocationSelectorFrame import LocationSelectorFrame
# from PopulationStatistics import PopulationStatistics
# from db.DBQueries import DBQueries
# from db.CitiesDBQueries import CitiesDBQueries
# from db.DistrictDBQueries import DistrictDBQueries
# from db.PopulationDBQueries import PopulationDBQueries

class StatisticsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bölgesel İstatistik Raporu")
        self.root.geometry("450x450")

        # Veritabanı bağlantıları
        self.country_db = CountryDBQueries()
        self.city_db = CitiesDBQueries()
        self.district_db = DistrictDBQueries()
        self.pop_db = PopulationDBQueries()

        self.arayuzu_olustur()

    def arayuzu_olustur(self):
        # 1. ORTAK LOKASYON BİLEŞENİNİ ÇAĞIRIP EN ÜSTE KOYUYORUZ
        self.location_selector = LocationSelectorFrame(
            self.root, self.country_db, self.city_db, self.district_db
        )
        self.location_selector.pack(pady=15)

        # 2. HESAPLA BUTONU
        btn_hesapla = ttk.Button(self.root, text="İstatistikleri Getir", command=self.istatistik_hesapla)
        btn_hesapla.pack(pady=10, ipady=5, ipadx=10)

        # 3. SONUÇLARIN GÖSTERİLECEĞİ ŞIK BİR ÇERÇEVE (LabelFrame)
        self.result_frame = ttk.LabelFrame(self.root, text=" Analiz Sonuçları ")
        self.result_frame.pack(pady=15, padx=30, fill="both", expand=True)

        # Başlangıçta boş duran etiketler (Labels)
        self.lbl_toplam = ttk.Label(self.result_frame, text="Toplam Nüfus: -", font=("Helvetica", 12, "bold"))
        self.lbl_toplam.pack(pady=10)

        self.lbl_kadin = ttk.Label(self.result_frame, text="Kadın Oranı: -", font=("Helvetica", 11))
        self.lbl_kadin.pack(pady=5)

        self.lbl_erkek = ttk.Label(self.result_frame, text="Erkek Oranı: -", font=("Helvetica", 11))
        self.lbl_erkek.pack(pady=5)

    def istatistik_hesapla(self):
        # Ortak bileşenden verileri çekiyoruz!
        selected_ids = self.location_selector.get_selected_ids()

        if selected_ids is None:
            messagebox.showwarning("Eksik Seçim", "Lütfen Ülke, Şehir ve İlçe seçimlerini eksiksiz yapın.")
            return

        c_id, city_id, dist_id = selected_ids

        # Seçilen ilçenin nüfus verisini veritabanından çekiyoruz (Az önce yazdığımız metod)
        ilce_nufusu_listesi = self.pop_db.get_population_by_district(dist_id)

        # Eğer o ilçede hiç kimse yoksa uyarı verip değerleri sıfırlayalım
        if len(ilce_nufusu_listesi) == 0:
            messagebox.showinfo("Bilgi", "Seçilen ilçede henüz kayıtlı nüfus bulunmamaktadır.")
            self.lbl_toplam.config(text="Toplam Nüfus: 0")
            self.lbl_kadin.config(text="Kadın Oranı: %0")
            self.lbl_erkek.config(text="Erkek Oranı: %0")
            return

        # VERİYİ İSTATİSTİK UZMANI SINIFIMIZA GÖNDERİYORUZ
        istatistik_uzmani = PopulationStatistics(ilce_nufusu_listesi)
        oranlar = istatistik_uzmani.calculate_gender_percentages()

        # HESAPLANAN VERİLERLE ARAYÜZÜ GÜNCELLİYORUZ
        self.lbl_toplam.config(text=f"Toplam Nüfus: {istatistik_uzmani.toplam_kisi} Kişi")
        self.lbl_kadin.config(text=f"Kadın Oranı: %{oranlar['Kadın']}")
        self.lbl_erkek.config(text=f"Erkek Oranı: %{oranlar['Erkek']}")