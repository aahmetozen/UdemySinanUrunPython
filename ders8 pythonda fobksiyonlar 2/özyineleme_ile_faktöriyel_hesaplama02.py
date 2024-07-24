def faktöriyel(n):
    if n==0:
        return 1
    else:
        return n * faktöriyel(n-1)
def main():
    print("5!",faktöriyel(5))
    print("1!", faktöriyel(1))
    print("0!", faktöriyel(0))
main()
