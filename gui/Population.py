import tkinter as tk
from tkinter import ttk, messagebox

from database.CitiesDBQueries import CitiesDBQueries
from database.CountryDBQueries import CountryDBQueries
from database.DistrictDBQueries import DistrictDBQueries
from database.PopulationDBQueries import PopulationDBQueries
from gui.LocationSelectorFrame import LocationSelectorFrame


# Sınıflarını import et (Kendi dosya yollarına göre düzenle)
# from db.DBQueries import DBQueries
# from db.CitiesDBQueries import CitiesDBQueries
# from db.DistrictDBQueries import DistrictDBQueries
# from db.PopulationDBQueries import PopulationDBQueries

class PopulationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Nüfus Kayıt Sistemi")
        self.root.geometry("400x350")

        # Veritabanı bağlantılarını başlatıyoruz
        # (Sınıf adlarını kendi koduna göre ayarlarsın)
        self.country_db = CountryDBQueries()
        self.city_db = CitiesDBQueries()
        self.district_db = DistrictDBQueries()
        self.pop_db = PopulationDBQueries()

        # İsimlerden ID'leri bulmak için hafıza sözlükleri
        self.country_map = {}
        self.city_map = {}
        self.district_map = {}

        self.arayuzu_olustur()

    def arayuzu_olustur(self):
        # 1. ORTAK LOKASYON BİLEŞENİNİ ÇAĞIRIP EKRANA YERLEŞTİRİYORUZ
        self.location_selector = LocationSelectorFrame(
            self.root, self.country_db, self.city_db, self.district_db
        )
        # Bu paneli en üste (row=0) yerleştiriyoruz
        self.location_selector.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        # --- YAŞ ---
        ttk.Label(self.root, text="Yaş:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_age = ttk.Entry(self.root, width=28)
        self.entry_age.grid(row=3, column=1, padx=10, pady=10)

        # --- CİNSİYET ---
        ttk.Label(self.root, text="Cinsiyet:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.combo_gender = ttk.Combobox(self.root, values=["Kadın", "Erkek"], state="readonly", width=25)
        self.combo_gender.grid(row=4, column=1, padx=10, pady=10)

        # --- ÇALIŞAN / ÖĞRENCİ (Checkbox) ---
        self.var_working = tk.IntVar()
        self.var_student = tk.IntVar()

        ttk.Checkbutton(self.root, text="Çalışıyor", variable=self.var_working).grid(row=5, column=0, padx=10, pady=5)
        ttk.Checkbutton(self.root, text="Öğrenci", variable=self.var_student).grid(row=5, column=1, padx=10, pady=5,
                                                                                   sticky="w")

        # --- KAYDET BUTONU ---
        btn_save = ttk.Button(self.root, text="Nüfusa Ekle", command=self.veriyi_kaydet)
        btn_save.grid(row=6, column=0, columnspan=2, pady=20)

    def veriyi_kaydet(self):
        try:
            # Kutulardaki verileri alıyoruz ve sözlüklerden ID'lerini çözüyoruz
            c_id = self.country_map[self.combo_country.get()]
            city_id = self.city_map[self.combo_city.get()]
            dist_id = self.district_map[self.combo_district.get()]
            age = int(self.entry_age.get())
            gender = self.combo_gender.get()
            is_working = self.var_working.get()  # 0 veya 1 döner
            is_student = self.var_student.get()  # 0 veya 1 döner

            if not gender:
                raise ValueError("Cinsiyet seçilmedi!")

            # Veritabanına gönderiyoruz
            self.pop_db.insert_population(c_id, city_id, dist_id, age, gender, is_working, is_student)

            # Kullanıcıya bilgi veriyoruz
            messagebox.showinfo("Başarılı", "Kişi sisteme başarıyla eklendi!")

            # Formu temizliyoruz (Yaş kutusunu)
            self.entry_age.delete(0, tk.END)

        except KeyError:
            messagebox.showerror("Hata", "Lütfen Ülke, Şehir ve İlçe seçimlerini tam yapın.")
        except ValueError:
            messagebox.showerror("Hata", "Yaş kısmına sadece sayı girin ve tüm alanları doldurun.")


# --- UYGULAMAYI ÇALIŞTIRMA ---
if __name__ == "__main__":
    root = tk.Tk()
    app = PopulationGUI(root)
    root.mainloop()