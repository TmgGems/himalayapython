def prod(num1,num2):
    print("The multiple of both value is :",num1*num2)


x=prod(2,3)
print(f"The solution  when nothing is returned is: {x}")#if nothing is returned form above then it gives the None

print("*******************")
print("************When returned************")
def prod(num1,num2):
    return(num1*num2)

x=prod(2,3)
print(f"The solution is: {x}")#here the returned value is taken
