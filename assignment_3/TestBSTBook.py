# Lihong
# implementation of TestDLinkedList class and related operations

from assignment_3 import Book
from assignment_3 import BSTBook

HarryPotter = Book.Book(1000000000001, 2250, 'Harry Potter', 'JK.R')
GameOfThrone = Book.Book(1000000000002, 2400, 'GameOfThrone', 'J.R.R.M')
TheThreeBodyProblem = Book.Book(1000000000003, 1500, 'TheThreeBodyProblem', 'Liu')
DataStructure = Book.Book(1000000000004, 2400, 'DataStructure', 'JK.R')


BookTree = BSTBook.BST(HarryPotter)

BookTree.insert(GameOfThrone)
BookTree.insert(TheThreeBodyProblem)
BookTree.insert(DataStructure)

print(BookTree.find(1000000000001))
print(BookTree.find(1000000000005))

BookTree.printAuthor('JK.R')


BookTree.printBooks()
