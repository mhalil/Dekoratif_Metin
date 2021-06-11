alf= {"a0" : "#####", "a1" : "#   #", "a2" : "#####", "a3" : "#   #", "a4" : "#   #", "h0" : "#   #", "h1" : "#   #",  "h2" : "#####", "h3" : "#   #", "h4" : "#   #", "i0" : "  #  ", "i1" : "     ", "i2" : "  #  ", "i3" : "  #  ", "i4" : "  #  ", "l0" : "#    ", "l1" :"#    ", "l2" : "#    ", "l3" : "#    ", "l4" : "#####"}

mkod = [] # yazılan metine karşılık gelen harf kodları, yazdırmaya hazırlamak için sırayla bu listeye eklenecek.
sayac = 0
sonuc = ""

girdi = input("metni yazın: ")  #halil
girdi = girdi.lower()

for _ in range(5):
    for harf in girdi:
        mkod.append(alf[harf + str(sayac)])
        mkod.append(" ")
    mkod.append("\n")
    sayac += 1
    
print(mkod)

    
for i in mkod:
    sonuc += i

# sonuc = sonuc.replace("#", "-") # "#" işareti yerine başka bir karakter kullanmak istersek burada ayarlayarak kullanabiliriz.
                      
print(sonuc)

