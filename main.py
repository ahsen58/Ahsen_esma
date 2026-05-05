import tkinter as tk
from tkinter import ttk, messagebox

from gui.MainMenu import MainMenu
from gui.Population import PopulationGUI

if __name__ == "__main__":
    ana_pencere = tk.Tk()

    # Ana menü sınıfımızı başlatıyoruz
    uygulama = MainMenu(ana_pencere)

    # Programı sürekli açık tutan ana döngü
    ana_pencere.mainloop()
  
