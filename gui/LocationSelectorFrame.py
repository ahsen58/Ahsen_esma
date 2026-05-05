import tkinter as tk
from tkinter import ttk


class LocationSelectorFrame(ttk.Frame):
    def __init__(self, parent, country_db, city_db, district_db, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.country_db = country_db
        self.city_db = city_db
        self.district_db = district_db

        self.country_map = {}
        self.city_map = {}
        self.district_map = {}

        self.arayuzu_olustur()
        self.ulkeleri_yukle()

    def arayuzu_olustur(self):
        ttk.Label(self, text="Ülke:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.combo_country = ttk.Combobox(self, state="readonly", width=25)
        self.combo_country.grid(row=0, column=1, padx=5, pady=5)
        self.combo_country.bind("<<ComboboxSelected>>", self.sehirleri_yukle)

        ttk.Label(self, text="Şehir:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.combo_city = ttk.Combobox(self, state="readonly", width=25)
        self.combo_city.grid(row=1, column=1, padx=5, pady=5)
        self.combo_city.bind("<<ComboboxSelected>>", self.ilceleri_yukle)

        ttk.Label(self, text="İlçe:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.combo_district = ttk.Combobox(self, state="readonly", width=25)
        self.combo_district.grid(row=2, column=1, padx=5, pady=5)

    def ulkeleri_yukle(self):
        ulkeler = self.country_db.get_all_countries()
        self.country_map = {u.name: u.id for u in ulkeler}
        self.combo_country['values'] = list(self.country_map.keys())

    def sehirleri_yukle(self, event):
        ulke_id = self.country_map[self.combo_country.get()]
        sehirler = self.city_db.get_cities_by_country(ulke_id)
        self.city_map = {s.name: s.id for s in sehirler}

        self.combo_city['values'] = list(self.city_map.keys())
        self.combo_city.set('')
        self.combo_district.set('')
        self.combo_district['values'] = []

    def ilceleri_yukle(self, event):
        sehir_id = self.city_map[self.combo_city.get()]
        ilceler = self.district_db.get_districts_by_city(sehir_id)
        self.district_map = {i.name: i.id for i in ilceler}

        self.combo_district['values'] = list(self.district_map.keys())
        self.combo_district.set('')

    def get_selected_ids(self):
        try:
            c_id = self.country_map[self.combo_country.get()]
            city_id = self.city_map[self.combo_city.get()]
            dist_id = self.district_map[self.combo_district.get()]
            return c_id, city_id, dist_id
        except KeyError:
            return None