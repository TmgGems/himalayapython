def smart_division(func):
    def wrapper(a,b):
        if b==0:
            return "Could not divide"
        else:
            return func(a,b)
    return wrapper

@smart_division
def division(a,b):
    return a/b
    
y=division(4,2)
print(y)
print(division(2,0))