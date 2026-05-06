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
        self.root.geometry("420x450")
        self.root.configure(bg="#fce4ec")
        self.country_db = CountryDBQueries()
        self.city_db = CitiesDBQueries()
        self.district_db = DistrictDBQueries()
        self.pop_db = PopulationDBQueries()
        self.arayuzu_olustur()

    def arayuzu_olustur(self):
        cerceve = tk.Frame(self.root, bg="#fce4ec")
        cerceve.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            cerceve,
            text="Nüfus Ekleme Ekranı",
            font=("Helvetica", 14, "bold"),
            bg="#fce4ec",
            fg="#880e4f"
        ).grid(row=0, column=0, columnspan=2, pady=15)

        self.location_selector = LocationSelectorFrame(
            cerceve, self.country_db, self.city_db, self.district_db
        )
        self.location_selector.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

        tk.Label(cerceve, text="Yaş:", bg="#fce4ec", fg="#880e4f", font=("Helvetica", 11)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_age = tk.Entry(cerceve, width=28, bg="#f8bbd0", fg="#880e4f", relief="flat", font=("Helvetica", 11))
        self.entry_age.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(cerceve, text="Cinsiyet:", bg="#fce4ec", fg="#880e4f", font=("Helvetica", 11)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.combo_gender = ttk.Combobox(cerceve, values=["Kadın", "Erkek"], state="readonly", width=25)
        self.combo_gender.grid(row=3, column=1, padx=10, pady=10)

        self.var_working = tk.IntVar()
        self.var_student = tk.IntVar()
        tk.Checkbutton(cerceve, text="Çalışıyor", variable=self.var_working, bg="#fce4ec", fg="#880e4f", selectcolor="#f8bbd0", font=("Helvetica", 10)).grid(row=4, column=0, padx=10, pady=5)
        tk.Checkbutton(cerceve, text="Öğrenci", variable=self.var_student, bg="#fce4ec", fg="#880e4f", selectcolor="#f8bbd0", font=("Helvetica", 10)).grid(row=4, column=1, padx=10, pady=5, sticky="w")

        tk.Button(
            cerceve,
            text="Nüfusa Ekle",
            command=self.veriyi_kaydet,
            bg="#ce93d8",
            fg="white",
            font=("Helvetica", 12, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8
        ).grid(row=5, column=0, columnspan=2, pady=20)

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