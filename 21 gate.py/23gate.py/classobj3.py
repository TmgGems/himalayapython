class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
    def number_of_pages(self):
        return len(self.pages)
    def add_pages(self,page):
        self.pages.append(page)

    def __str__(self):
        