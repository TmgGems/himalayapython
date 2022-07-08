def funcn(num):
    main=[]
    odd=[]
    even=[]
    duplicate=[]
    for x in range(num):
        N=int(input("Enter the number: "))
        def main():
            main.append(N)
            return main
        def even():
            if N%2==0:
                even.append(N)
                return even
        def odd():
            if N%2!=0:
                odd.append(N)
                return odd
        
        def dupliacte():
            if N==N:
                duplicate.append(N)
                return duplicate
n=int(input("Enter how many times you want:"))
funcn(n)
print(even())
print(odd())
print(duplicate())
print(main())