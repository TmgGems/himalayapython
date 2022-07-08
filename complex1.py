def square_root_of_sum(func,num1,num2):
    return func(num1,num2)**0.5

def add(num1,num2):
    return num1+num2

print(square_root_of_sum(add,10,5))