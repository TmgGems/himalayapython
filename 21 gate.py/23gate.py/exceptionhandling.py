try:
    n1=int(input("Enter the number:"))
    n2=int(input("Enter the number:"))
except ValueError:
    print("Cannot convert to integer:")
except NameError:
    print("Variable not defined")
else:
    print(n1+n2)