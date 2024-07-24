# belirli döngü
n = 1
while n <= 10:
    print(n)
    n += 1

# -----------------------
# belirli döngü örnek2
n = 1
karar = int(input())
while n <= karar:
    print(n)
    n += 1

# -----------------------
# belirsiz döngü
karar = False
while not karar:
    giris = int(input())
    if giris == 999:
        karar = True
    else:
        print(giris)