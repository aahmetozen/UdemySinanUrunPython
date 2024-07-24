for i in range(16):
    print("{0:3} {1:16}".format(i, 10**i))

# ------------------------
print("{} {} yi seviyor".format("ali","ayşe"))
print("{} {} yaşında bir {}dur".format("ahmet","19","futbolcu"))

# ------------------------------
for i in range(10):
    print(i,end=" ")
    if i ==5:
        i=20
        print("({})".format(i),end=" ")
print()

# --------------------------------
kelime=input("bir kelime yazınız")
for harf in kelime:
    print(harf)
