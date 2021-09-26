# Yazıtipi İsimlerini Gösteren Bir Seçim Menüsü oluşturuldu.
print("""
Kullanılabilir Yazıtipleri;
**************************
 1. Banner3          6. Isometric2
 2. Colossal         7. Isometric3
 3. Doh              8. Isometric4
 4. Epic             9. Standard
 5. Isometric1      10. Univers
""")

secim = input("Listedeki yazı tiplerinden birini seçin (Sadece sayı değeri girin) : ") # Kullanıcıdan Menü seçeneklerinden birini seçmesi isteniyor.
yazitipi_sec = {"1" : "banner3", "2" : "colossal" , "3" : "doh" ,"4" : "epic" , "5" : "isometric1", "6" : "isometric2", "7" : "isometric3" , "8" : "isometric4" , "9" : "standard", "10" : "univers"}                       # Seçime karşılık gelen yazıtipini sözlük ile belirle.
yazitipi = yazitipi_sec[secim]                      # Seçilen yazıtipinin adı.
yazitipi_yolu = "fonts/" + yazitipi + ".flf"        # Yazıtipinin tam yolu.

def ky():                                           # Yazıtipini oluşturan karakterlerin yuksekligi (her karakterin kaç satırdan oluştuğunu) hesaplayan fonksiyon.
    yukseklik = 0                                   # Karakter Yüksekliği (satır sayısı) 
          
    with open (yazitipi_yolu , "r", encoding="utf-8") as dosya:
        liste = dosya.readlines()                   # Yazıtipi dosyasını oku, Listele.
        
        for oge in liste:                           # harf yüksekliği hesaplanıyor.
            if (oge[-3:] == "@@\n"):                # ekseriyetle satır sonları @ ile, karakter sonları (sınırları) @@ ile bitiriliyor. Zaman zaman @ yerine # kullanıldığı da oluyor.
                break                               # harf yüksekliğinin sınırı ile karşılaşınca işlemi durdur.

            elif ((oge[-2:] == "@\n") or (oge[-3:] == "$@\n") or (oge == "\x7f\x7f\x7f\x7f\x7f@\n")):       # satırın tamamına, son 2 ve 3 karakterilerine bakarak karakter yüksekliği sonlanmış mı? kontrol et.
                yukseklik += 1                      # karakter yüksekliği sonlanmamışsa (sınırlanmamışsa) yükseklik değerini bir artır.
                 
    return (yukseklik+1)                            # Yazıtipinin karakter yüksekliğini fonksiyona değer olarak ata.

def listele():                                      # Belirtilen yazitipi dosyasındaki "@\n" ve "@@\n" karakterlerini silerek liste oluştur.
    alfabe_kodlari = list()

    with open (yazitipi_yolu , "r", encoding="utf-8") as dosya:
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

def alfabe_sozluk():
    karakterler = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÂÖÜâöüβ""" # Yazıtipi dosyalarında bulunan sıralı karakter bilgisi.
    karakterler_standard = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÂÖÜâöüβ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſˇ˘˙˛˝""" # "STANDARD" isimli Yazıtipi dosyasında bulunan sıralı karakter bilgisi.
    
    krt_yuk = ky()                                  # Karakter YÜksekliği değerini ky() fonksiyonun çalıştırarak hesapla ve krt_yuk değişkenine ata.
    alfabe_kod = listele()                          # Alfabeye ait kodları listele() fonksiyonun çalıştırarak hesapla ve alfabe_kod değişkenine ata.
    alfabe_key = list()                             # alfabe_key isimi boş bir liste oluştur.
    alfabe = dict()                                 # alfabe isimi boş bir sözlük yapısı oluştur.
    
    if secim == "9":
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

def sonuc():                                        # Kullanıcıdan Yazitipi menüsünden seçim yapmasını ve bir metin yazmasını isteyen; Yazılan metni, seçilen yazıtipi kodlarına çevirerek ekrana yazdıran fonksiyon.
    sozluk = alfabe_sozluk()                        # alfabe_sozluk() fonksiyonunu çalıştır ve sozluk isimli değişkene ata. 
    yuk = ky()                                      # ky() fonksiyonunu çalıştırarak, karakter (satır) yüksekliğini hesaplaya ve yuk isimli değişkene ata.
    girdi = input("Metni yazın: ")                  # Kullanıcıdan bir metin girmesini iste.
    sonuc = ""                                      # sonuc isimli boş bir string oluştur.
    
    if secim != "9":                                # "standard" isimli yazıtiplerinde daha az sayıda karakter var, eğer o yazıtipleri seçilirse Türkçe karakterler yerine diğer karakterleri kullan.
        turkce_karakterler = {"ç" : "c", "Ç" : "C", "ğ" : "g", "Ğ" : "G", "ı" : "i", "İ" : "I", "ş" : "s", "Ş" : "S"}       # hangi harfe yerine hangi hrf kullanılacak, onu belirle.

        for i in range(1, yuk+1):                   # Kullanıcının yazdığı metni sozluk yapısından sorgulayarak her karaktere karşılık gelen kodları sonuc isimli stringe ekleyen döngü yapısı.
            for harf in girdi:
                if harf in turkce_karakterler.keys():   # Girdi içerisinde Türkçe karakter varsa, kod hata vermesin alfabede ona yakın karakteri kullansın. Ör: ş yerine s, Ğ yerine G, ...vb
                    harf = turkce_karakterler[harf]
                sonuc += sozluk[harf + str(i)] + "   "
            sonuc += "\n"
    
    else:                                           # "standart" isimli yazıtipi içerisinden 331 karakter var. Bu durumda, girdide yazılan kelimeleri olduğu gibi (karakterleri değiştirmeden) kullan.
        for i in range(1, yuk+1):                   # Kullanıcının yazdığı metni sozluk yapısından sorgulayarak her karaktere karşılık gelen kodları sonuc isimli stringe ekleyen döngü yapısı.
            for harf in girdi:
                sonuc += sozluk[harf + str(i)] + "   "
            sonuc += "\n"

    print(sonuc.replace("$", " "))                  # sonuc isimli stringdeki (karakter sonlarındaki) $ karakterini silerek sonucu ekrna yazdır.

sonuc()                                             # sonuc() fonksiyonunu çalıştır.
