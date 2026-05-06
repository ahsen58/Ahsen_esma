import tkinter as tk
from tkinter import ttk, messagebox

from gui.Population import PopulationGUI
from gui.StatisticsGUI import StatisticsGUI






class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Nüfus Kayıt Sistemi - Ana Menü")
        self.root.geometry("350x250")
        self.root.configure(bg="#fce4ec")
        self.arayuzu_olustur()


    def arayuzu_olustur(self):
        lbl_baslik = tk.Label(self.root, text="Sisteme Hoş Geldiniz", font=("Helvetica", 16, "bold"), bg="#fce4ec",
                              fg="#880e4f")
        lbl_baslik.pack(pady=30)

        btn_ekle = tk.Button(self.root, text="1. Nüfus Ekleme Ekranı", command=self.nufus_ekrani_ac, bg="#ce93d8", fg="black")
        btn_ekle.pack(pady=10, fill='x', padx=50, ipady=5)
        btn_diger = tk.Button(self.root, text="2. İstatistikler", command=self.istatistik_ekrani_ac, bg="#ce93d8", fg="black")
        btn_diger.pack(pady=10, fill='x', padx=50, ipady=5)

    def nufus_ekrani_ac(self):
        yeni_pencere = tk.Toplevel(self.root)
        app = PopulationGUI(yeni_pencere)

    def istatistik_ekrani_ac(self):
        yeni_pencere = tk.Toplevel(self.root)
        app = StatisticsGUI(yeni_pencere)