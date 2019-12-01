from assignment_2 import DLinkedListADT
from assignment_2 import Book


HarryPotter = Book.Book('0001', 2250, 'Harry Potter')
GameOfThrone = Book.Book('0002', 2400, 'GameOfThrone')
TheThreeBodyProblem = Book.Book('0003', 1500, 'TheThreeBodyProblem')
DataStructure = Book.Book('0004', 2400, 'DataStructure')
BigData = Book.Book('0005', 1400, 'BigData')
BookInstance = DLinkedListADT.DlinkedListADT()
BookInstance.addFirst(HarryPotter)
BookInstance.addLast(GameOfThrone)
BookInstance.addLast(TheThreeBodyProblem)
BookInstance.addLast(DataStructure)
BookInstance.addLast(BigData)
BookInstance.printNextList()

def ConvertToArray(data):
    total = data.size()
    if data is None or total == 0:
        raise Exception('Invalid Input!')
    BookArray = []
    num = 0
    while num < total:
        temp = data.deleteFirst()
        BookArray.append(temp.Book)
        data.addLast(temp.Book)
        temp = data.deleteFirst()
        data.addLast(temp.Book)
        num += 2
    if total % 2 != 0:
        temp = data.deleteLast()
        data.addFirst(temp.Book)
    return BookArray


def TestConvertToArray(data):
    BookArray = ConvertToArray(data)
    total = len(BookArray)
    for i in range(0, total):
        print('Array:', BookArray[i].isbn)
    data.printNextList()


TestConvertToArray(BookInstance)

