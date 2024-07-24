def tree(yukseklik):
    satir=0 # First row, from the tree
    while satir<yukseklik: # Draw one row for ever
        sayac=0
        while sayac<yukseklik-satir:
            print(end=" ")
            sayac+=1
        sayac=0
        while sayac<2*satir+1:
            print(end="*")
            sayac+=1
        print()
        satir+=1
def main():
    yukseklik=int(input("Ağacın yüksekliğini giriniz: "))
    tree(yukseklik)
main()