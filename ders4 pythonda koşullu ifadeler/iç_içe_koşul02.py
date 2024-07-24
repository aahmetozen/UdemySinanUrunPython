deger = int(input("Lütfen  0….10  aralığında bir tamsayı giriniz: "))

if deger >= 0 and deger <= 10:   #ikili koşul kontrolü
    print("aralıkta")
print("tamamlandı")


deger = int(input("Lütfen  0….10  aralığında bir tamsayı giriniz: "))
if deger >= 0: #ilk kontrol
    if deger <= 10: #ikinci kontrol
        print("aralıkta")
    print("tamamlandı")