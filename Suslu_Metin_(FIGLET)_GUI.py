import tkinter as tk
from tkinter import ttk
from tkinter import *

def secilen_yazitipi():
    secim  = yazitipi.get()
    if secim == 1:
       return "Banner3"

    elif secim == 2:
       return  "Colossal"
    
    elif secim == 3:
       return  "Doh"
    
    elif secim == 4:
       return  "Epic"
    
    elif secim == 5:
       return  "Isometric1"
    
    elif secim == 6:
       return  "Isometric2"
    
    elif secim == 7:
       return  "Isometric3"
    
    elif secim == 8:
       return  "Isometric4"
    
    elif secim == 9:
       return  "Standard"
    
    elif secim == 10:
       return  "Univers"

# Buton Fonksiyonları
def donustur():
   cikti.insert(tk.END,girdi.get() + "\n")
   for _ in range(5):
      cikti.insert(tk.END,yazitipi.get() + "\n")

def temizle():
   girdi.delete(0,tk.END)
   cikti.delete("1.0",tk.END)

def kaydet():
   pass

def kopyala():    # Cikti penceresindeki Metni Panoya (clipboard'da) kopyalar
    pencere.clipboard_clear()  # Optional.
    pencere.clipboard_append(cikti.get('1.0', tk.END).rstrip())

pencere = tk.Tk()
pencere.geometry("505x450+500+300")
pencere.resizable(0, 0)
pencere.title(".:: Metni Süsle [ FIGLET ] ::.")

etiket_girdi = tk.Label(pencere, text = "Dönüştürülecek Metni Yazın:")
etiket_girdi.place(x=10, y=10)

girdi = tk.Entry(pencere, width=25)
girdi.focus()
girdi.place(x=10, y=40)

aciklama = tk.Label(text = "Kullanmak istediğiniz Yazıtipini seçin.")
aciklama.place(x=240, y=10)

# Yazıtipi Listesi
secili_yazitipi = tk.StringVar()
yazitipi = ttk.Combobox(pencere, textvariable=secili_yazitipi, width=28)
yazitipi["values"] = ("Banner3", "Colossal", "Doh", "Epic", "Isometric1", "Isometric2", "Isometric3", "Isometric4", "Standard", "Univers")
yazitipi['state'] = 'readonly'
yazitipi.set("Banner3")
yazitipi.place(x=240, y=40)

# Sonucun yazdırılacağı Metin ekranı 
cikti = tk.Text(pencere, width=60, height=19)
cikti.place(x=10, y=80)

# Butonlar
buton_genisligi = 8

btn_donustur = tk.Button(pencere, 
                        text="Dönüştür",
                        width=buton_genisligi,
                        command=donustur)
btn_donustur.place(x=10, y=415)                     

btn_temizle = tk.Button(pencere, 
                        text="Temizle",
                        width=buton_genisligi,
                        command=temizle)
btn_temizle.place(x=108, y=415)  

btn_kopyala = tk.Button(pencere, 
                        text="Kopyala",
                        width=buton_genisligi,
                        command=kopyala)
btn_kopyala.place(x=206, y=415)  

btn_kaydet = tk.Button(pencere, 
                        text="Kaydet",
                        width=buton_genisligi,
                        command=kaydet)
btn_kaydet.place(x=304, y=415)                     

btn_kapat = tk.Button(pencere, 
                        text="Kapat",
                        width=buton_genisligi,
                        command=quit)
btn_kapat.place(x=402, y=415) 

pencere.mainloop()