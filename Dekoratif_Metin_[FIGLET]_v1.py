# Aşağıdaki kodların amaci, kullanıcının seçmiş olduğu yazıtipine ait karakterleri, satırlar halinde okuyarak sözlük haline getirmektir.

karakterler = """é!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÂÖÜâöüβ""" # Yazıtipi dosyalarında bulunan sıralı (en fazla) karakter bilgisi.

# print(karakterler)

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
9. Standard
10. Univers
""")

secim = input("Listedeki yazı tiplerinden birini seçin (Sadece sayı değeri girin) : ") # "input" ile kullanıcıdan seçim yapması istenecek.

yazitipi = {"1" : "banner3", "2" : "colossal" , "3" : "doh" ,"4" : "epic" , "5" : "isometric1", "6" : "isometric2", "7" : "isometric3" , "8" : "isometric4" , "9" : "standard" , "10" : "univers"} # seçime karşılık gelen yazıtipini sözlük ile belirle.

font = yazitipi[secim]
ky = 0      # Karakter Yüksekliği (satır sayısı) 

# krk_sirasi = 0
# karakter = karakterler[krk_sirasi]
# indis = 1   # sözlüğe klenecek olan karakterlerin (key) yanına eklenecek saıyı tanımlayacak. örneğin "a1", "a2", ... vb
# anahtar = karakter + str(indis) # sozluk anahtari. ornegin a1, a2,...vb
indeks = 0      # font_liste2 nin indeks bilgisi. Sözlüge ekleme işleminde  kullanılacak.
font_liste2 = []
alfabe = dict()

if secim not in yazitipi:
    print("Yanlış seçim yaptınız! Listede bulunan, geçerli bir sayı değeri girmelisiniz !")

else:
    print(f"Seçilen yazıtipi : {font}")                                  
    font_dosyasi = "fonts/" + font + ".flf"

    with open (font_dosyasi , "r", encoding="utf-8") as belge:
        font_liste = belge.readlines()      # readlines()  ile font dosyasını içeriğini okuyor ve liste olarak alıyoruz.

        # print(font_liste)

        for oge in font_liste:      # harf yüksekliği hesaplanıyor.
             if ((oge[-3:] == " @\n") or (oge[-3:] == "$@\n") or (oge == "\x7f\x7f\x7f\x7f\x7f@\n")):
                 ky += 1  

             elif (oge[-3:] == "@@\n"):
                break       # harf yüksekliğinin hesaplanma işlemi bu satır ile sonlanıyor.
        
        print(f"{font} yazıtipinin karakter yüksekliği {ky+1} satırdır.")


        for eleman in font_liste:       # karakter kodlarının başlangıcını belirtip numaralandıracağız. 
            if (eleman[-2:] == "@\n"):
                if (eleman[-2:] == "@\n"):
                    font_liste2.append(eleman[:-2])

                elif (eleman[-3:] == "@@\n"):
                    font_liste2.append(eleman[:-3])
     
        # for j in font_liste2:       # font dosyası başlangıcındaki koda ait olmayan bilgiler temizleniyor.
        #     if (j[-2:] != "@\n"):
        #         font_liste2.remove(j)
        #     elif (j[-2:] == "@\n"):
        #         break

        for k in karakterler:       # karakterlere sayı numarası eklenip alfabe adlı sözlüğe kaydediliyor.
            for l in range(1,ky+1):
                if (font_liste2[indeks][-2:] != "@\n") and (font_liste2[indeks][-3:] != "@@\n"):
                    alfabe[k+str(l)] = font_liste2[indeks][:-2]
                    indeks += 1
                elif (font_liste2[indeks][-3:] == "@@\n"):
                    alfabe[k+str(l)] = font_liste2[indeks][:-2]
                    indeks += 1
       
        # KONTROL AMACLI ÇALIŞTIR.
        # print(font_liste2)
        # print(alfabe)

        # for i in font_liste2:
        #     print(i)

# AŞAĞIDAKİ KODLAR, NİHAİ SÖZLÜK OLUŞTUKTAN SONRA, GİRDİ (KEY) DEĞERLERİNE KARŞILIK GELEN DEĞERLERİ (VALUE) BİR ARAYA GETİRİP EKRANA YAZDIRACAK

# sonuc = ""
# girdi = input("Metni yazın: ").lower()

# for i in range(1, ky+1): 
#     for harf in girdi:
#         sonuc += alfabe[harf + str(i)] + "   "
#     sonuc += "\n"

# print(sonuc)