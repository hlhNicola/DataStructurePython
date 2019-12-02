# Lihong
# implementation of TestStackADT

from assignment_2 import StackADT
from assignment_2 import Book

book_1 = Book.Book("9780133761313", 354, "Intro to Java Programming")
book_2 = Book.Book("9770133751312", 414, "Intro to Python Programming")

testStack = StackADT.StackADT(100)
print("Current queue is empty:", testStack.isEmpty())
print("Book to be push()ed to stack: ISBN:", book_1.isbn, "pages:", book_1.pages, "title:", book_1.title)
testStack.push(book_1)
print("First item in stack: ISBN:", testStack.peek().isbn, "pages:", testStack.peek().pages, "title:", testStack.peek().title)
print("Current stack is empty:", testStack.isEmpty())
print("Book to be push()ed to stack: ISBN:", book_2.isbn, "pages:", book_2.pages, "title:", book_2.title)
testStack.push(book_2)
print("Number of elements in stack:", 2)
removeItem_1 = testStack.pop()
removeItem_2 = testStack.pop()
print("Pop()ed Item: ISBN:", removeItem_1.Book.isbn, "pages:", removeItem_1.Book.pages, "title:", removeItem_1.Book.title)
print("Pop()ed Item: ISBN:", removeItem_2.Book.isbn, "pages:", removeItem_2.Book.pages, "title:", removeItem_2.Book.title)
print("Current stack is empty:", testStack.isEmpty())
