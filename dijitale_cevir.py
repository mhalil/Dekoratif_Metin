#h = """
##   #
##   # 
######
##   #
##   #"""
#
#h0="#   #"
#h1="#   #"
#h2="#####"
#h3="#   #"
#h4="#   #"
#
#a0="#####"
#a1="#   #"
#a2="#####"
#a3="#   #"
#a4="#   #"
#
#l0="#    "
#l1="#    "
#l2="#    "
#l3="#    "
#l4="#####"
#
#i0="  #  "
#i1="     "
#i2="  #  "
#i3="  #  "
#i4="  #  "

#h=["#   #", "#   #", "#####", "#   #", "#   #"]


alf= {"a0" : "#####", "a1" : "#   #", "a2" : "#####", "a3" : "#   #", "a4" : "#   #", "h0" : "#   #", "h1" : "#   #",  "h2" : "#####", "h3" : "#   #", "h4" : "#   #"}

metin = [] # yazılan metine karşılık gelen harf kodları, yazdırmaya hazırlamak için sırayla bu listeye eklenecek.

girdi = input("metni yazın: ")  #halil

for harf in girdi:
    print(alf[harf + "0"]) # "0", "1", ...vb deerleri yerine indeks değeri eklenmeli

