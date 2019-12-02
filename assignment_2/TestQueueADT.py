from assignment_2 import QueueADT
from assignment_2 import Book

book_1 = Book.Book("9780133761313", 354, "Intro to Java Programming")
book_2 = Book.Book("9770133751312", 414, "Intro to Python Programming")

testQueue = QueueADT.QueueADT(100)
print("Current queue is empty:", testQueue.sEmpty())
print("Book to be enqueue()ed to queue: ISBN:", book_1.isbn, "pages:", book_1.pages, "title:", book_1.title)
testQueue.enQueue(book_1)
print("First item in queue: ISBN:", testQueue.peek().isbn, "pages:", testQueue.peek().pages, "title:", testQueue.peek().title)
print("Current queue is empty:", testQueue.sEmpty())
print("Book to be added to queue: ISBN:", book_2.isbn, "pages:", book_2.pages, "title:", book_2.title)
testQueue.enQueue(book_2)
print("Number of elements in queue:", 2)
removeItem_1 = testQueue.deQueue()
removeItem_2 = testQueue.deQueue()
print("Removed Item: ISBN:", removeItem_1.Book.isbn, "pages:", removeItem_1.Book.pages, "title:", removeItem_1.Book.title)
print("Removed Item: ISBN:", removeItem_2.Book.isbn, "pages:", removeItem_2.Book.pages, "title:", removeItem_2.Book.title)
print("Current queue is empty:", testQueue.sEmpty())
