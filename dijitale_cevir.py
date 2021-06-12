alf= {"a0" : "#####", "a1" : "#   #", "a2" : "#####", "a3" : "#   #", "a4" : "#   #", "h0" : "#   #", "h1" : "#   #",  "h2" : "#####", "h3" : "#   #", "h4" : "#   #", "ı0" : "#", "ı1" : "#", "ı2" : "#", "ı3" : "#", "ı4" : "#", "i0" : "#", "i1" : " ", "i2" : "#", "i3" : "#", "i4" : "#", "l0" : "#    ", "l1" :"#    ", "l2" : "#    ", "l3" : "#    ", "l4" : "#####"}

mkod = [] # yazılan metine karşılık gelen harf kodları, yazdırmaya hazırlamak için sırayla bu listeye eklenecek.
sayac = 0
sonuc = ""

girdi = input("metni yazın: ")  #halil
girdi = girdi.lower()

for _ in range(5):  # büyük har fkullanıca bu satırda hata veriyor.
    for harf in girdi:
        mkod.append(alf[harf + str(sayac)])
        mkod.append(" ") # karakterler arasına eklenecek boşluk ya da özel karakter
    mkod.append("\n")
    sayac += 1
    
for i in mkod:
    sonuc += i

# sonuc = sonuc.replace("#", "*") # "#" karakterini değiştirmek isterseniz, yerine kullaınmasını istediğiniz karakteri bura belirtin.
                      
print(sonuc)

