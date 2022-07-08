def eve(num):
    even=[]
    for i in range(num):
        num=int(input("Enter the number :"))
        if num%2==0:
            even.append(num)
    return even
n=int(input("How many times you want to enter:"))
print(eve(n))