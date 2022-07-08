def outer(func):
    def inner():
        print("Hello Students!")
        func()
        print("Byee...")
    return inner

 @outer
def welcome():
   print("Welcome Students!")

# a=outer(welcome)
# a()
welcome()