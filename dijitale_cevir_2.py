# Öncelikle Yazıtiplerinden birer numune harf ya da sayı gösterip,  seçim yapılmasını isteyeceğiz.
print("""
Yazıtipi Seçenekleri:
1. banner3
2. colossal
3. doh
4. univers
""")
f_name = input("yazıtipi seçin: ") # Kullanmak istediğimiz Yazıtipini seçmek için kullanıcıdan eçim yapmasını istiyoruz.

if f_name == "1":
    f_name = "banners3"

elif f_name == "2":
    f_name = "colossal"

elif f_name == "3":
    f_name = "doh"

elif f_name == "4":
    f_name = "univers"

else:               
    f_name = "univers"

font_name = "fonts/" + f_name + ".txt" # Menüden yapılan seçime göre, açılacak olan dosya adını oluşturuyoruz.

# print(font_name)


with open (font_name, "r", encoding="utf-8") as dosya:
    print(dosya.read())