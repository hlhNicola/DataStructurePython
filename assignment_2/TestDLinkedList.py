# Lihong
# implementation of TestDLinkedList class and related operations

from assignment_2 import Book
from assignment_2 import DLinkedListADT

HarryPotter = Book.Book('0001', 2250, 'Harry Potter')
GameOfThrone = Book.Book('0002', 2400, 'GameOfThrone')
TheThreeBodyProblem = Book.Book('0003', 1500, 'TheThreeBodyProblem')
DataStructure = Book.Book('0004', 2400, 'DataStructure')
RickMorty = Book.Book('1000', 2400, 'RickMorty')
SuperSystem = Book.Book('1001', 2400, 'SuperSystem')

WrongPagesGameOfThrone = Book.Book('0002', '1200', 'GameOfThrone')
WrongIsbnGameOfThrone = Book.Book('0000000000000000002', '1200', 'GameOfThrone')
WrongTitleGameOfThrone = Book.Book('0002', '1200', True)

# HarryPotter.bookValidation()
# GameOfThrone.bookValidation()
# TheThreeBodyProblem.bookValidation()
# WrongPagesGameOfThrone.bookValidation()
# WrongIsbnGameOfThrone.bookValidation()
# WrongTitleGameOfThrone.bookValidation()

Book = DLinkedListADT.DlinkedListADT()
# Book.addFirst(HarryPotter)
# Book.addFirst(HarryPotter)
Book.addFirst(DataStructure)
# Book.deleteFirst()
Book.addLast(GameOfThrone)
# Book.addLast(GameOfThrone)
Book.addLast(TheThreeBodyProblem)
# Book.deleteFirst()
# Book.deleteLast()
# Book.deleteAll()
Book.printNextList()
# Book.printPrevList()
# print('Book Size:', Book.size())
# print('The title of the target book to find is:', Book.findBook('0001').title)
# print('The title of the max cost book is:', Book.returnMaxCostBook().title)

print("MergeList Test")
SecondBook = DLinkedListADT.DlinkedListADT()

SecondBook.addLast(RickMorty)
SecondBook.addLast(SuperSystem)

SecondBook.printNextList()
print("----")
Book.MergeList(SecondBook)
Book.printNextList()
