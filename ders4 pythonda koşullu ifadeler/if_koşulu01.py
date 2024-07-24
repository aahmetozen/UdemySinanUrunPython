print("lütfen bölme için iki sayı giriniz")
bolum=int(input("lütfen bölme için ilk sayıyı girinz"))
bolen=int(input("lütfen bölme için ikinci sayıyı giriniz"))
if bolen!=0: # eğer bölen sıfır değilse
    print(bolum,"/",bolen,"=",bolum/bolen)
if bolen == 0: # sıfıra bölmeye çalışıldığında
    print("sıfıra bölme yapılamaz")