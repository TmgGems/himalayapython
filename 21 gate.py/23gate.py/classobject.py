#Noun->object
#adjective->attribute,property
#verb(action)->behavior,method
class Book:
    def __init__(self,page):
        self.page=page
    def read(self):
        print(f"Page number {self.page} is being read")

c=Book(200)
# print(c.page)
# print(c.read())
c.read()

