import tkinter as tk
from tkinter import ttk
from tkinter import *

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
# Kullanıcı metin yazıp, Listeden Yazitipi seçtikten sonra, Yazılan metni, seçilen yazıtipi kodlarına çevirerek cikti ekranına yazdıran fonksiyon.
def donustur():                                        

    yuk = ky()                                  # ky() fonksiyonunu çalıştırarak, karakter (satır) yüksekliğini hesaplaya ve yuk isimli değişkene ata.
    sozluk = alfabe_sozluk()                    # alfabe_sozluk() fonksiyonunu çalıştır ve sozluk isimli değişkene ata.                                       
    girdi_metni = girdi.get()                   # Kullanıcıdan bir metin girmesini iste.
    sonuc = ""                                  # sonuc isimli boş bir string oluştur.
    
    y_tipi_adi = yazitipi.get()                 # Açılır listede seçili olan yazıtipi adı

    if y_tipi_adi != "Standard":                     # "standard" isimli yazıtiplerinde daha az sayıda karakter var, eğer o yazıtipleri seçilirse Türkçe karakterler yerine diğer karakterleri kullan.
        turkce_karakterler = {"ç" : "c", "Ç" : "C", "ğ" : "g", "Ğ" : "G", "ı" : "i", "İ" : "I", "ş" : "s", "Ş" : "S"}       # hangi harfe yerine hangi hrf kullanılacak, onu belirle.

        for i in range(1, yuk+1):               # Kullanıcının yazdığı metni sozluk yapısından sorgulayarak her karaktere karşılık gelen kodları sonuc isimli stringe ekleyen döngü yapısı.
            for harf in girdi_metni:
                if harf in turkce_karakterler.keys():   # Girdi içerisinde Türkçe karakter varsa, kod hata vermesin alfabede ona yakın karakteri kullansın. Ör: ş yerine s, Ğ yerine G, ...vb
                    harf = turkce_karakterler[harf]
                sonuc += sozluk[harf + str(i)] + "   "
            sonuc += "\n"
    
    else:                                       # "standart" isimli yazıtipi içerisinden 331 karakter var. Bu durumda, girdide yazılan kelimeleri olduğu gibi (karakterleri değiştirmeden) kullan.
        for i in range(1, yuk+1):               # Kullanıcının yazdığı metni sozluk yapısından sorgulayarak her karaktere karşılık gelen kodları sonuc isimli stringe ekleyen döngü yapısı.
            for harf in girdi_metni:
                sonuc += sozluk[harf + str(i)] + "   "
            sonuc += "\n"
        
    suslu_metin = sonuc.replace("$", " ")        # sonuc isimli stringdeki (karakter sonlarındaki) $ karakterini silerek sonucu ekrna yazdır.
    cikti.insert(tk.END, suslu_metin)

def donustur_dikey():

    yuk = ky()                                  # ky() fonksiyonunu çalıştırarak, karakter (satır) yüksekliğini hesaplaya ve yuk isimli değişkene ata.
    sozluk = alfabe_sozluk()                    # alfabe_sozluk() fonksiyonunu çalıştır ve sozluk isimli değişkene ata.                                       
    girdi_metni = girdi.get()                   # Kullanıcıdan bir metin girmesini iste.
    sonuc = ""                                  # sonuc isimli boş bir string oluştur.
    
    y_tipi_adi = yazitipi.get()                 # Açılır listede seçili olan yazıtipi adı

    if y_tipi_adi != "Standard":                     # "standard" isimli yazıtiplerinde daha az sayıda karakter var, eğer o yazıtipleri seçilirse Türkçe karakterler yerine diğer karakterleri kullan.
        turkce_karakterler = {"ç" : "c", "Ç" : "C", "ğ" : "g", "Ğ" : "G", "ı" : "i", "İ" : "I", "ş" : "s", "Ş" : "S"}       # hangi harfe yerine hangi hrf kullanılacak, onu belirle.

        for i in range(1, yuk+1):               # Kullanıcının yazdığı metni sozluk yapısından sorgulayarak her karaktere karşılık gelen kodları sonuc isimli stringe ekleyen döngü yapısı.
            for harf in girdi_metni:
                if harf in turkce_karakterler.keys():   # Girdi içerisinde Türkçe karakter varsa, kod hata vermesin alfabede ona yakın karakteri kullansın. Ör: ş yerine s, Ğ yerine G, ...vb
                    harf = turkce_karakterler[harf]
                sonuc += sozluk[harf + str(i)] + "   "
            sonuc += "\n"
   
    else:                                       # "standart" isimli yazıtipi içerisinden 331 karakter var. Bu durumda, girdide yazılan kelimeleri olduğu gibi (karakterleri değiştirmeden) kullan.
        for i in range(1, yuk+1):               # Kullanıcının yazdığı metni sozluk yapısından sorgulayarak her karaktere karşılık gelen kodları sonuc isimli stringe ekleyen döngü yapısı.
            for harf in girdi_metni:
                sonuc += sozluk[harf + str(i)] + "   "
            sonuc += "\n"
        
    suslu_metin = sonuc.replace("$", " ")        # sonuc isimli stringdeki (karakter sonlarındaki) $ karakterini silerek sonucu ekrna yazdır.
    
    for harf in suslu_metin:
        cikti.insert(tk.END, harf)

def temizle():
   girdi.delete(0,tk.END)
   cikti.delete("1.0",tk.END)
   cikti.configure(width = 60)
   pencere.geometry("505x450+500+300")

def kaydet():
   pass

def kopyala():    # Cikti penceresindeki Metni Panoya (clipboard'da) kopyalar
    pencere.clipboard_clear()  # Optional.
    pencere.clipboard_append(cikti.get('1.0', tk.END).rstrip())

# ARABİRİM
pencere = tk.Tk()
pencere.geometry("505x450+500+300")
pencere.resizable(0, 0)
pencere.title(".:: Dekoratif Metin [ FIGLET ] ::.")

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
cikti = tk.Text(pencere, width=57, height=17, wrap=NONE)
cikti.place(x=30, y=80)

dikey_kaydirma = Scrollbar(pencere)
dikey_kaydirma.place(x=10, y=80, height=300)
dikey_kaydirma["orient"] = "vertical"
dikey_kaydirma.config(command=cikti.yview)
cikti['yscrollcommand'] = dikey_kaydirma.set

yatay_kaydirma = Scrollbar(pencere)
yatay_kaydirma.place(x=30, y=380, width=450)
yatay_kaydirma["orient"] = "horizontal"
yatay_kaydirma.config(command=cikti.xview)
cikti['xscrollcommand'] = yatay_kaydirma.set

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
                        text="donustur_dikey",
                        width=buton_genisligi,
                        command=donustur_dikey)
btn_kaydet.place(x=304, y=415)                     

btn_kapat = tk.Button(pencere, 
                        text="Kapat",
                        width=buton_genisligi,
                        command=quit)
btn_kapat.place(x=402, y=415)


pencere.mainloop()