#x=int(input("Enter the base value:"))
#y=int(input("Enter the power value:"))
#print("The power  {y} of base {x} is",x**y)
def power(a,b):
    result=1
    for x in range(b):
            result*=a
    return result
x=int(input("Enter the base value:"))
y=int(input("Enter the power value:"))
x=power(x,y)
print("The required answer is :",x)