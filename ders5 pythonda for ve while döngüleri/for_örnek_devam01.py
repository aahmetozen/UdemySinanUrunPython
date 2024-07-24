kelime = input("Cümle Giriniz: ")
sesliHarfSayisi = 0
for c in kelime:
    if c == "A" or c == "a" or c == "E" or c == "e"\
    or c == "I" or c == "i" or c == "O" or c == "o":
        print(c, ", ", sep="", end="")
        sesliHarfSayisi += 1
print(" (", sesliHarfSayisi, " sesli)", sep="")

# -----------------------
# iç içe döngüler
# Satır oluşturmak için
sayi = int(input("Lütfen tablo ölçüsünü giriniz: "))
for satir in range(1, sayi + 1):
    print("Satır  # ", satir)

# -----------------------
# iç içe 3'lü döngü
#ABC harflerinin farklı permütasyonu:
for ilk in "ABC":
    for ikinci in "ABC":
        if ikinci != ilk:
            for ucuncu in "ABC":
                if ucuncu != ilk and ucuncu != ikinci:
                    print(ilk + ikinci + ucuncu)
