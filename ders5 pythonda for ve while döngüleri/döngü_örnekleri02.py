#girilen sayının faktöriyelini hesaplayan program
faktöriyel=1
sayac=1
sayı=int(input("bir sayı giriniz"))
while sayac<=sayı:
    faktöriyel*=sayac
    sayac+=1
print(sayı,"sayının faktöriyeli:",faktöriyel)

