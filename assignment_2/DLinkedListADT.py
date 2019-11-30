class Node:
    def __init__(self, initdata):
        self.Book = initdata
        self.next = None
        self.prev = None
        return


class DlinkedListADT:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
        return

    def addFirst(self, data):
        if self.findBook(data.isbn) is not None:
            raise Exception('Do not add duplicate book!')
        n = Node(data)
        if self.front is None:
            self.front = n
            self.rear = n
        else:
            n.next = self.front
            self.front.prev = n
            self.front = n
        self.length += 1

    def addLast(self, data):
        if self.findBook(data.isbn) is not None:
            raise Exception('Do not add duplicate book!')
        n = Node(data)
        if self.front is None:
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            n.prev = self.rear
            self.rear = n
        self.length += 1

    def deleteFirst(self):
        if self.front is None:
            raise Exception('The list is empty')
        n = Node(self.front)
        if self.front is not None & self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.length -= 1
        return n.Book

    def deleteLast(self):
        if self.front is None:
            raise Exception('The list is empty')
        n = Node(self.front)
        if self.front is not None & self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.length -= 1
        return n.Book

    def deleteAll(self):
        while self.length > 0:
            self.deleteLast()

    def size(self):
        return self.length

    def printNextList(self):
        n = self.front
        while n is not None:
            print('ISBN: ', n.Book.isbn, ', Pages: ', n.Book.pages, ', Title: ', n.Book.title)
            n = n.next

    def printPrevList(self):
        n = self.rear
        while n is not None:
            print('ISBN: ', n.Book.isbn, ', Pages: ', n.Book.pages, ', Title: ', n.Book.title)
            n = n.prev

    def findBook(self, isbn):
        n = self.front
        while n is not None & n.Book.isbn != isbn:
            n = n.next
        if n is None:
            print('Isbn', isbn, ' Not Found')
            return None
        else:
            return n.Book

    def returnMaxCostBook(self):
        n = self.front
        maxCost = 0
        maxCostBook = n.Book
        while n is not None:
            cost = n.pages * 0.005
            if cost > maxCost:
                maxCost = cost
                maxCostBook = n.Book
            n = n.next
        return maxCostBook

