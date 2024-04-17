import tkinter as tk
from tkinter import messagebox
from tkinter import *
import ttkbootstrap as ttk
import glob

## FONKSİYONLAR
# Yazıtipini oluşturan karakterlerin yuksekligi (her karakterin kaç satırdan oluştuğunu) hesaplayan fonksiyon.
def ky():                                           
    yukseklik = 0                                   # Karakter Yüksekliği (satır sayısı) 
    y_tipi = "fonts/" + yazitipi.get().lower() + ".flf"      
    with open (y_tipi , "r", encoding="utf-8") as dosya:
        liste = dosya.readlines()                   # Yazıtipi dosyasını oku, Listele.
        
        for oge in liste:                           # harf yüksekliği hesaplanıyor.
            if (oge[-3:] == "@@\n"):                # ekseriyetle satır sonları @ ile, karakter sonları (sınırları) @@ ile bitiriliyor. Zaman zaman @ yerine # kullanıldığı da oluyor.
                break                               # harf yüksekliğinin sınırı ile karşılaşınca işlemi durdur.

            elif ((oge[-2:] == "@\n") or (oge[-3:] == "$@\n") or (oge == "\x7f\x7f\x7f\x7f\x7f@\n")):       # satırın tamamına, son 2 ve 3 karakterilerine bakarak karakter yüksekliği sonlanmış mı? kontrol et.
                yukseklik += 1                      # karakter yüksekliği sonlanmamışsa (sınırlanmamışsa) yükseklik değerini bir artır.
                 
    return (yukseklik+1)                            # Yazıtipinin karakter yüksekliğini fonksiyona değer olarak ata.

# Belirtilen yazitipi dosyasındaki "@\n" ve "@@\n" karakterlerini silerek liste oluştur.
def listele():                                      
    alfabe_kodlari = list()
    y_tipi = "fonts/" + yazitipi.get().lower() + ".flf"
    with open (y_tipi , "r", encoding="utf-8") as dosya:
        liste = dosya.readlines()
        for i in liste:
            if (i[-2:] != "@\n"):
                if ( (i[-2:] == "#\n") and (i[-3:] != "##\n")):     # sonu @ ile bitmeyen karakterlerde ekseriyetle @ yerine # kullanılıyor. "doh" yazitipinde @ işareti, aynı karakterden oluşturulduğu için bitiş parametresi # ile belirtilmiş.
                    alfabe_kodlari.append(i[:-2])

                elif (i[-3:] == "##\n"):
                    alfabe_kodlari.append(i[:-3])

            else:
                if ( (i[-2:] == "@\n") and (i[-3:] != "@@\n")):     
                    alfabe_kodlari.append(i[:-2])
                
                elif (i[-3:] == "@@\n"):
                    alfabe_kodlari.append(i[:-3])
                  
    return alfabe_kodlari                           # Alfabeyi oluşturan kodlara ait listeyi, fonksiyona değer olarak ata.
print("listele:", listele)
# Yazıtipi dosyalarında bulunan sıralı karakter bilgisi.
def alfabe_sozluk():
    y_tipi = "fonts/" + yazitipi.get().lower() + ".flf"
    karakterler = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÂÖÜâöüβ""" 
    karakterler_standard = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÂÖÜâöüβ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſˇ˘˙˛˝""" # "STANDARD" isimli Yazıtipi dosyasında bulunan sıralı karakter bilgisi.
    
    krt_yuk = ky()                                  # Karakter YÜksekliği değerini ky() fonksiyonun çalıştırarak hesapla ve krt_yuk değişkenine ata.
    alfabe_kod = listele()                          # Alfabeye ait kodları listele() fonksiyonun çalıştırarak hesapla ve alfabe_kod değişkenine ata.
    alfabe_key = list()                             # alfabe_key isimi boş bir liste oluştur.
    alfabe = dict()                                 # alfabe isimi boş bir sözlük yapısı oluştur.
    
    if y_tipi == "fonts/standard.flf":
        for k in karakterler_standard:              # Karakterlere sayı numarası eklenip alfabe_key listesine kaydeden döngü yapısı.
            for l in range(1,krt_yuk+1):            # Sayılar 1'den başlayarak karakter (satır) yüksekliğine kadar devam edecek.
                alfabe_key.append(k+str(l))         # listeye ekle. Ör: A1, A2, A3, ..., z1, z2, z3...vb
    else:        
        for k in karakterler:                       # Karakterlere sayı numarası eklenip alfabe_key listesine kaydeden döngü yapısı.
            for l in range(1,krt_yuk+1):            # Sayılar 1'den başlayarak karakter (satır) yüksekliğine kadar devam edecek.
                alfabe_key.append(k+str(l))         # listeye ekle. Ör: A1, A2, A3, ..., z1, z2, z3...vb

    for i in range(len(alfabe_kod)):                # alfabe_kod listesindeki öğeleri, alfabe_key listesindek öğelerle sırasına uygun olarak eşleştirip alfabe isimli sözlüğe ekleyen döngü yapısı. Ör: {'a1' : '## # #' }
        alfabe[alfabe_key[i]] = alfabe_kod[i]
    
    return alfabe                                   # Oluşturulan alfabe isimli sözlüğü fonksiyona değer olarak ata.

## BUTON Fonksiyonları
def donustur_yatay():           # Kullanıcı metin yazıp, Listeden Yazitipi seçtikten sonra, Yazılan metni, seçilen yazıtipi kodlarına çevirerek cikti ekranına YATAY olarak yazdıran fonksiyon.

    yuk = ky()                  # ky() fonksiyonunu çalıştırarak, karakter (satır) yüksekliğini hesaplaya ve yuk isimli değişkene ata.
    sozluk = alfabe_sozluk()    # alfabe_sozluk() fonksiyonunu çalıştır ve sozluk isimli değişkene ata.                                       
    girdi_metni = girdi.get()   # kullanıcının girdiği metni al.
    sonuc = ""                  # sonuc isimli boş bir string oluştur.
    
    y_tipi_adi = yazitipi.get() # Açılır listede seçili olan yazıtipi adı

    if y_tipi_adi != "Standard":    # "standard" isimli yazıtiplerinde daha az sayıda karakter var, eğer o yazıtipleri seçilirse Türkçe karakterler yerine diğer karakterleri kullan.
        turkce_karakterler = {"ç" : "c", "Ç" : "C", "ğ" : "g", "Ğ" : "G", "ı" : "i", "İ" : "I", "ş" : "s", "Ş" : "S",  "ö" : "o", "Ö" : "O", "ü" : "u", "Ü" : "U"}       # hangi harfe yerine hangi hrf kullanılacak, onu belirle.

        for i in range(1, yuk+1):   # Kullanıcının yazdığı metni sozluk yapısından sorgulayarak her karaktere karşılık gelen kodları sonuc isimli stringe ekleyen döngü yapısı.
            for harf in girdi_metni:
                if harf in turkce_karakterler.keys():   # Girdi içerisinde Türkçe karakter varsa, kod hata vermesin alfabede ona yakın karakteri kullansın. Ör: ş yerine s, Ğ yerine G, ...vb
                    harf = turkce_karakterler[harf]
                sonuc += sozluk[harf + str(i)] + "   "
            sonuc += "\n"
    
    else:                           # "standart" isimli yazıtipi içerisinden 331 karakter var. Bu durumda, girdide yazılan kelimeleri olduğu gibi (karakterleri değiştirmeden) kullan.
        for i in range(1, yuk+1):   # Kullanıcının yazdığı metni sozluk yapısından sorgulayarak her karaktere karşılık gelen kodları sonuc isimli stringe ekleyen döngü yapısı.
            for harf in girdi_metni:
                sonuc += sozluk[harf + str(i)] + "   "
            sonuc += "\n"
        
    dekoratif_metin = sonuc.replace("$", " ")   # sonuc isimli stringdeki (karakter sonlarındaki) $ karakterini silerek sonucu ekrna yazdır.
    cikti.insert(tk.END, dekoratif_metin + "\n")

def donustur_dikey():           # Kullanıcı metin yazıp, Listeden Yazitipi seçtikten sonra, Yazılan metni, seçilen yazıtipi kodlarına çevirerek cikti ekranına DİKEY olarak yazdıran fonksiyon.
   
    yuk = ky()                  # ky() fonksiyonunu çalıştırarak, karakter (satır) yüksekliğini hesaplaya ve yuk isimli değişkene ata.
    sozluk = alfabe_sozluk()    # alfabe_sozluk() fonksiyonunu çalıştır ve sozluk isimli değişkene ata.                                       
    girdi_metni = girdi.get()   # kullanıcının girdiği metni al.
    y_tipi_adi = yazitipi.get() # Açılır listede seçili olan yazıtipi adı

    yeni_girdi = ""

    if y_tipi_adi != "Standard":    # "standard" isimli yazıtiplerinde daha az sayıda karakter var, eğer o yazıtipleri seçilirse Türkçe karakterler yerine diğer karakterleri kullan.
        turkce_karakterler = {"ç" : "c", "Ç" : "C", "ğ" : "g", "Ğ" : "G", "ı" : "i", "İ" : "I", "ş" : "s", "Ş" : "S", "ö" : "o", "Ö" : "O", "ü" : "u", "Ü" : "U"}       # hangi harfe yerine hangi hrf kullanılacak, onu belirle.

        for harf in girdi_metni:    # Kullanıcının yazdığı metinde Türkçe karakter varsa, bu karakterleri değiştir ve yeni_girdi degiskenine ekle. Ör: ç => c, ş => s
            if harf not in turkce_karakterler.keys():
                yeni_girdi += harf
            
            else:
                yeni_girdi += turkce_karakterler[harf]

        for harf in yeni_girdi:
            for sayi in range(1, yuk+1):
                sonuc = sozluk[harf + str(sayi)].replace("$", " ")
                sonuc_harf = sonuc + "\n"
                cikti.insert(tk.END, sonuc_harf)
            cikti.insert(tk.END, "\n")
            
    
    else:                           # "standart" isimli yazıtipi içerisinden 331 karakter var. Bu durumda, girdide yazılan kelimeleri olduğu gibi (karakterleri değiştirmeden) kullan.
        for harf in girdi_metni:
            for sayi in range(1, yuk+1):
                sonuc = sozluk[harf + str(sayi)].replace("$", " ")
                sonuc_harf = sonuc + "\n"
                cikti.insert(tk.END, sonuc_harf)
            cikti.insert(tk.END, "\n")

def temizle():  # girdi ve çıktı ekranlarını temizleyen fonksiyon.
   girdi.delete(0,tk.END)
   cikti.delete("1.0",tk.END)

def kaydet():   # çıktı ekranındaki dekoratif metni "Dekoratif_Metin.txt" ismi ile aynı dizine kaydeden fonksiyon.
    metin = girdi.get()
    dekoratif_metin = int(cikti.index("end")[:-2]) - 2
    if dekoratif_metin > 0:
        with open("Dekoratif_Metin.txt", "w", encoding="UTF-8") as dosya:
            dosya.write("'" + metin + "' Metninin Dekoratif hali aşağıdadır;\n\n" + cikti.get("1.0","end"))
    else:
        messagebox.showinfo("Kaydedilecek Veri Yok!","Dekoratif Metin Üretilmediği için, kayıt işlemi gerçekleştirilemiyor.")

def kopyala():  # Cikti penceresindeki Metni Panoya (clipboard'da) kopyalar
    pencere.clipboard_clear()
    pencere.clipboard_append(cikti.get('1.0', tk.END).rstrip())

def yt_liste():
    yt = glob.glob("fonts/*.flf")   # yazitipleri
    liste = []
    for tip in yt:
        tip = tip.replace("fonts\\", "")
        tip = tip.replace(".flf", "")
        liste.append(tip.title())
        liste.sort()
    return tuple(liste)

# ARABİRİM
pencere = tk.Tk()
pencere.geometry("735x650+500+200")
pencere.resizable(0, 0)
pencere.title(".:: Dekoratif Metin [ FIGLET ] ::.")

etiket_girdi = tk.Label(pencere, text = "Dönüştürülecek Metni Yazın:")
etiket_girdi.place(x=10, y=10)

girdi = ttk.Entry(pencere, width=70, bootstyle="success")
girdi.focus()
girdi.place(x=10, y=40)

aciklama = tk.Label(text = "Kullanmak istediğiniz Yazıtipini seçin.")
aciklama.place(x=455, y=10)

# Yazıtipi Listesi
secili_yazitipi = tk.StringVar()
yazitipi = ttk.Combobox(pencere, textvariable=secili_yazitipi, width=40, bootstyle="success")
yazitipi["values"] = yt_liste()     # yt_liste() fonksiyonu ile elde edilen yazıtipleri açılır listeye atanıyor
yazitipi['state'] = 'readonly'
yazitipi.set(yazitipi["values"][0]) # ilk değer varsayılan olarak belirleniyor
yazitipi.place(x=455, y=40)

# Sonucun yazdırılacağı Metin ekranı
cikti = tk.Text(pencere, width=85, height=30, wrap=NONE, font="Courier 10") # Consolas, Courier, CourierNew, Fixedsys, yazıtipleri de uygun
cikti.place(x=30, y=80)

dikey_kaydirma = ttk.Scrollbar(pencere, orient="vertical", bootstyle="secondary-round")
dikey_kaydirma.place(x=10, y=80, height=500)
dikey_kaydirma.config(command=cikti.yview)
cikti['yscrollcommand'] = dikey_kaydirma.set

yatay_kaydirma = ttk.Scrollbar(pencere, orient="horizontal", bootstyle="secondary-round")
yatay_kaydirma.place(x=30, y=590, width=700)
yatay_kaydirma.config(command=cikti.xview)
cikti['xscrollcommand'] = yatay_kaydirma.set

# Butonlar
buton_genisligi = 14
x_konum = 28
x_artis = 115

btn_donustur_y = ttk.Button(pencere, 
                        text="Yatay",
                        width=buton_genisligi,
                        command=donustur_yatay)
btn_donustur_y.place(x=x_konum, y=610)                     

btn_donustur_d = ttk.Button(pencere, 
                        text="Dikey",
                        width=buton_genisligi,
                        command=donustur_dikey)
btn_donustur_d.place(x=x_konum + x_artis, y=610)  

btn_temizle = ttk.Button(pencere, 
                        bootstyle="success",
                        text="Temizle",
                        width=buton_genisligi,
                        command=temizle)
btn_temizle.place(x=x_konum + x_artis * 2, y=610)  

btn_kopyala = ttk.Button(pencere,
                        bootstyle="success", 
                        text="Kopyala",
                        width=buton_genisligi,
                        command=kopyala)
btn_kopyala.place(x=x_konum + x_artis * 3, y=610)  

btn_kaydet = ttk.Button(pencere,
                        bootstyle="dark", 
                        text="Kaydet",
                        width=buton_genisligi,
                        command=kaydet)
btn_kaydet.place(x=x_konum + x_artis * 4, y=610)                     

btn_kapat = ttk.Button(pencere,
                        bootstyle="danger", 
                        text="Kapat",
                        width=buton_genisligi,
                        command=quit)
btn_kapat.place(x=x_konum + x_artis * 5, y=610)


pencere.mainloop()
