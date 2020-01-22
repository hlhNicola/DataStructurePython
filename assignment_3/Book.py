# Lihong
# implementation of Bookclass

class Book:
    def __init__(self, isbn, pages, title, author):
        self.isbn = isbn
        self.pages = pages
        self.title = title
        self.author = author

    def getKey(self):
        return self.isbn

    def getAuthor(self):
        return self.author

    def bookValidation(self):
        if len(self.isbn) is not 13:
            raise Exception('Isbn should be 13 digits!')
        if type(self.title) != str:
            raise Exception('Title type should be string!')
        if type(self.author) != str:
            raise Exception('Author type should be string!')
        if type(self.pages) != int:
            raise Exception('Pages type should be Integer!')
        else:
            print('ISBN:', self.isbn, 'is valid!')

