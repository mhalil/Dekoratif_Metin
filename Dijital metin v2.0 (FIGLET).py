# kodların amacı, belirtilen FLF dosyasındaki fazlalıkları silip sade, kullanılabilir sözlük yapısı oluşturmaktır.

print("""
Kullanılabilir Yazıtipleri;
**************************
1. Banner3
2. Colossal
3. Doh
4. Epic
5. Isometric1
6. Isometric2
7. Isometric3
8. Isometric4
9. Univers
""")

secim = input("Listedeki yazı tiplerinden birini seçin (Sadece sayı değeri girin) : ") # "input" ile kullanıcıdan seçim yapması istenecek.
yazitipi_sec = {"1" : "banner3", "2" : "colossal" , "3" : "doh" ,"4" : "epic" , "5" : "isometric1", "6" : "isometric2", "7" : "isometric3" , "8" : "isometric4" , "9" : "univers"} # seçime karşılık gelen yazıtipini sözlük ile belirle.
yazitipi = yazitipi_sec[secim]
yazitipi_yolu = "fonts/" + yazitipi + ".flf"

def ky():       # Yazıtipini oluşturan karakterlerin yuksekligi (her karakterin kaç satırdan oluştuğunu) hesaplayan fonksiyon.
    yukseklik = 0          # Karakter Yüksekliği (satır sayısı) 
          
    with open (yazitipi_yolu , "r", encoding="utf-8") as dosya:
        liste = dosya.readlines()
        # print(liste)
        for oge in liste:      # harf yüksekliği hesaplanıyor.
            if (oge[-3:] == "@@\n"):
                break       # harf yüksekliğinin hesaplanma işlemi bu satır ile sonlanıyor.

            elif ((oge[-2:] == "@\n") or (oge[-3:] == "$@\n") or (oge == "\x7f\x7f\x7f\x7f\x7f@\n")):
                yukseklik += 1  
                 
    # print(f"{yazitipi} yazıtipinin karakter yüksekliği {yukseklik+1} satırdır.")
    return (yukseklik+1)

def listele():      # belirtilen yazitipi dosyasındaki "@\n" ve "@@\n" karakterlerini silerek liste oluştur.
    alfabe_kodlari = list()

    with open (yazitipi_yolu , "r", encoding="utf-8") as dosya:
        liste = dosya.readlines()
        for i in liste:
            if (i[-2:] != "@\n"):
                pass
            else:
                if ( (i[-2:] == "@\n") and (i[-3:] != "@@\n")):
                    alfabe_kodlari.append(i[:-2])
                
                elif (i[-3:] == "@@\n"):
                    alfabe_kodlari.append(i[:-3])
                  
    # print(alfabe_kodlari)
    return alfabe_kodlari

def alfabe_sozluk():
    karakterler = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÂÖÜâöüβ""" # Yazıtipi dosyalarında bulunan sıralı (en fazla) karakter bilgisi.
    
    krt_yuk = ky()
    alfabe_kod = listele()
    alfabe_key = list()
    alfabe = dict()
    
    for k in karakterler:       # karakterlere sayı numarası eklenip alfabe adlı sözlüğe kaydediliyor.
        for l in range(1,krt_yuk+1):
            alfabe_key.append(k+str(l))

    for i in range(len(alfabe_kod)):
        alfabe[alfabe_key[i]] = alfabe_kod[i]

    # print(alfabe_kod)
    # print(alfabe_key)
    return alfabe

def sonuc():
    sozluk = alfabe_sozluk()
    yuk = ky()
    # girdi = input("Metni yazın: ")
    girdi = "Mustafa"
    sonuc = ""

    for i in range(1, yuk+1): 
        for harf in girdi:
            sonuc += sozluk[harf + str(i)] + "   "
        sonuc += "\n"

    print(sonuc.replace("$", " "))

# print(ky())
# print(listele())
# print(alfabe_sozluk())

# ky()
# listele()
# alfabe_sozluk()
sonuc()



