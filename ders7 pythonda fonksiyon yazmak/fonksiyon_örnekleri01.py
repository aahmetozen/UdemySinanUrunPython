def say():
    for i in range(1, 11):
        print(i, end=" ")
    print()
print("10’a kadar sayılıyor...")
say()
print("Tekrar 10’a kadar sayılıyor...")
say()

# ----------------
# başka bir örnek
def say_n(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()
print("10’a kadar sayılıyor...")
say_n(10)
print("5’e kadar sayılıyor...")
say_n(5)

# ---------------------
# başka bir örnek daha
def say_n(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()
for i in range(1, 11):
    say_n(i)