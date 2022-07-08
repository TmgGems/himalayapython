
from audioop import add


def calculator(operator,a,b):#a=10,b=15
    def add():
        return a+b
    def multiple():
        return a*b
    if operator=="+":
        return add
    elif operator=="*":
        return multiple
a=calculator("+",10,15) #a=add
print(a())
b=calculator("*",10,15)  #b=multiple
print(b())