from math import sqrt
# Kullanıcıdan değer alınıyor
sayi = float(input("Sayı Giriniz: "))
# Karakök hesaplanarak kok değişkenine aktarılıyor
kok = sqrt(sayi) # kök değişkenine sqrt fonksiyonunun sonucu aktarılmış
# Sonuçlar yazdırılıyor
print(sayi," sayısının karekökü" "=", kok)