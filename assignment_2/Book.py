# Lihong
# implementation of Bookclass

class Book:
    def __init__(self, isbn, pages, title):
        self.isbn = isbn
        self.pages = pages
        self.title = title

    def bookValidation(self):
        if len(self.isbn) > 13:
            raise Exception('Isbn should be not longer than 13 digits!')
        if type(self.title) != str:
            raise Exception('Title type should be string!')
        if type(self.pages) != int:
            raise Exception('Pages type should be Integer!')
        else:
            print('ISBN:', self.isbn, 'is valid!')
