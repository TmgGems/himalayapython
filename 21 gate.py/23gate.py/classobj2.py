
class Page:
    def __init__(self,page_number,content):
        self.content=content
        self.page_number=page_number

    def read(self):#instance method
        print(f"Reading {self.content} of page number{self.page_number}")

    @staticmethod
    def print_to_printer(content):#static method
        print("Printing...")
        print(content)
    def __str__(self):
        return self.content
    def __repr__(self):
        return self.content


#p=Page(1,"this is new paragraph.")
#p.read()
#Page.print_to_printer("This is a sentence.")

class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages

    def number_of_pages(self):
        return(len(self.pages))

pages=[]
for i in range(1,6):
   p=Page(i,f"This is paragraph{i}.")
   print(f"{pages} {p.page_number} {p.content}")
   pages.append(p)

b=Book("MAths",pages)
print(f"Number of pages:{b.number_of_pages()}")
