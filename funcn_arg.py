# def funcn(**kwargs):
#     print(kwargs)

# funcn(name="G",address="kav")
from numpy import prod

#***************************
#in reverse order
def funcn(name,address):
    print(f"Name:",name)
    print(f"address:",address)

pro={"name":"Gems","address":"Kavre"}
funcn(**pro)