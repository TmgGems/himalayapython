# def outer_func():
#     def first_child():
#         print("I am first child")
#     def second_child():
#         print("I am second child")
#     first_child()
#     second_child()

# outer_func()
def calculator(operator):
    def add(a,b):
        return a+b
    def product(a,b):
        return a*b
    if operator=="+":
        return add
    elif operator=="*":
        return product

totalsum=calculator("+")
multiplication=calculator("*")
print(totalsum(10,15))
print(multiplication(10,15))