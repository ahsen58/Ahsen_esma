import tkinter as tk
from tkinter import ttk, messagebox

from gui.Population import PopulationGUI


# Kendi dosyalarından gerekli sınıfları import etmeyi unutma
# from PopulationGUI import PopulationGUI

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Nüfus Kayıt Sistemi - Ana Menü")
        # Ekran boyutunu ayarlıyoruz
        self.root.geometry("350x250")

        self.arayuzu_olustur()

    def arayuzu_olustur(self):
        # Başlık Etiketi
        lbl_baslik = ttk.Label(self.root, text="Sisteme Hoş Geldiniz", font=("Helvetica", 16, "bold"))
        lbl_baslik.pack(pady=30)

        # 1. BUTON: Nüfus Ekleme Ekranını Açan Buton
        btn_ekle = ttk.Button(self.root, text="1. Nüfus Ekleme Ekranı", command=self.nufus_ekrani_ac)
        # fill='x' butonu yatayda uzatır, ipadx/ipady butonun iç boşluklarını büyütür
        btn_ekle.pack(pady=10, fill='x', padx=50, ipady=5)

        # 2. BUTON: Şimdilik boş duran 2. buton (İleride istatistik veya listeleme ekranı yaparsın)
        btn_diger = ttk.Button(self.root, text="2. İstatistikler (Yakında)", command=self.yakinda_mesaji)
        btn_diger.pack(pady=10, fill='x', padx=50, ipady=5)

    def nufus_ekrani_ac(self):
        # YENİ PENCERE AÇMA MANTIĞI:
        # tk.Tk() yerine tk.Toplevel() kullanıyoruz ki ana menüden bağımsız yeni bir alt pencere açılsın.
        yeni_pencere = tk.Toplevel(self.root)

        # Daha önce yazdığımız PopulationGUI sınıfını bu yeni pencerenin içine gömüyoruz
        app = PopulationGUI(yeni_pencere)

    def yakinda_mesaji(self):
        # İkinci buton tıklandığında şimdilik sadece bir bilgi mesajı versin
        messagebox.showinfo("Bilgi", "Bu ekran henüz yapım aşamasındadır.")