def decorate_function(func):
    def wrapper():
        print("Hello students")
        func()
        print("BYE BYE Students!")
    return wrapper
@decorate_function
def welcome():
    print("welcome Students!")
#a=decorate_function(welcome)
#a()
welcome() #wrapper is called