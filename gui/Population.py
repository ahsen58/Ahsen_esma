import tkinter as tk
from tkinter import ttk, messagebox

from database.CitiesDBQueries import CitiesDBQueries
from database.CountryDBQueries import CountryDBQueries
from database.DistrictDBQueries import DistrictDBQueries
from database.PopulationDBQueries import PopulationDBQueries
from gui.LocationSelectorFrame import LocationSelectorFrame




class PopulationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Nüfus Kayıt Sistemi")
        self.root.geometry("400x350")
        self.country_db = CountryDBQueries()
        self.city_db = CitiesDBQueries()
        self.district_db = DistrictDBQueries()
        self.pop_db = PopulationDBQueries()
        self.country_map = {}
        self.city_map = {}
        self.district_map = {}
        self.arayuzu_olustur()

    def arayuzu_olustur(self):
        self.location_selector = LocationSelectorFrame(
            self.root, self.country_db, self.city_db, self.district_db
        )
        self.location_selector.grid(row=0, column=0, columnspan=2, pady=10, padx=10)


        ttk.Label(self.root, text="Yaş:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_age = ttk.Entry(self.root, width=28)
        self.entry_age.grid(row=3, column=1, padx=10, pady=10)


        ttk.Label(self.root, text="Cinsiyet:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.combo_gender = ttk.Combobox(self.root, values=["Kadın", "Erkek"], state="readonly", width=25)
        self.combo_gender.grid(row=4, column=1, padx=10, pady=10)


        self.var_working = tk.IntVar()
        self.var_student = tk.IntVar()

        ttk.Checkbutton(self.root, text="Çalışıyor", variable=self.var_working).grid(row=5, column=0, padx=10, pady=5)
        ttk.Checkbutton(self.root, text="Öğrenci", variable=self.var_student).grid(row=5, column=1, padx=10, pady=5,
                                                                                   sticky="w")


        btn_save = ttk.Button(self.root, text="Nüfusa Ekle", command=self.veriyi_kaydet)
        btn_save.grid(row=6, column=0, columnspan=2, pady=20)

    def veriyi_kaydet(self):
        selected_ids = self.location_selector.get_selected_ids()

        if selected_ids is None:
            messagebox.showerror("Hata", "Lütfen Ülke, Şehir ve İlçe seçimlerini tam yapın.")
            return

        c_id, city_id, dist_id = selected_ids

        try:
            age = int(self.entry_age.get())
            gender = self.combo_gender.get()
            is_working = self.var_working.get()
            is_student = self.var_student.get()

            if not gender:
                raise ValueError

            self.pop_db.insert_population(c_id, city_id, dist_id, age, gender, is_working, is_student)
            messagebox.showinfo("Başarılı", "Kişi sisteme başarıyla eklendi!")
            self.entry_age.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Hata", "Lütfen yaş kısmına sadece sayı girin ve boş alan bırakmayın.")
