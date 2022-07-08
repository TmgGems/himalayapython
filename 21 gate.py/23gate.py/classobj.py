from email import contentmanager


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

p=Page(1,"this is new paragraph.")
p.read()
Page.print_to_printer("This is a sentence.")