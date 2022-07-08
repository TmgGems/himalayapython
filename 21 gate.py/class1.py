class Car:
    #initialiser function
    def __init__(self,model,color):
        self.c=color
        self.m=model
    
c=Car("2022","Blue")
print(c.m)
print(c.c)