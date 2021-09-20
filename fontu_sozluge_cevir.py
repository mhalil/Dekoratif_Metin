# print("""
# Bir Yazıtipi Seçin:
# 1.
# 2.
# 3.
# 4.
# 5.
# """)
karakterler = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÂÖÜâöüβ'

# print(karakterler[6])

font = "epic"                                   # "input" ile kullanıcıdan seçim yapması istenecek.
font_dosyasi = "fonts/" + font + ".txt"

hy = 0 # Harf Yüksekliği (satır sayısı)
sozluk = dict()
indis = 1

with open (font_dosyasi , "r") as belge:
    for satir in belge:                     # harf yüksekliği hesaplanıyor.
        if (satir[-4:] == "$$@\n"):
            hy += 1  

        elif (satir[-4:] == "$@@\n"):
            break                           # harf yüksekliğinin hesaplanma işlemi bitimi.
    

    # for satir in belge:                     # karakter kodlarının başlangıcını belirtip numaralandıracağız.
    #     if (satir[-4:] == "$@@\n"):
