#sayac = 1   # Başlangıç değeri kontrol değişkenine atanır.
#while sayac <= 5:  # İstenilen  değere  ulaşıp  ulaşmadığını  kontrol eder.
#    print("sayac değeri:",sayac)    # Sayaç değerini ekrana yazar.
#    sayac += 1  # Sayaç değerini 1 arttırır.

# ----------------------
sayac = 0
giris = "Y"
while giris != "N" and giris != "n":
    print(sayac)

    giris = input('''Devam etmek için "Y" – çıkmakiçin "N" giriniz: ''')
    if giris == "Y" or giris == "y":
        sayac += 1
    elif giris != "N" and giris != "n":
        print("" + giris + "geçerli bir giriş kodu değil")