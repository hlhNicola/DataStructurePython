# Lihong
# implementation of StackADT class and related operations

from assignment_2 import DLinkedListADT

class StackADT:

    def __init__(self, min):
        if min <= 0:
            raise Exception("No capacity!")
        self.items = DLinkedListADT.DlinkedListADT()
        self.capacity = min * 2

    def isEmpty(self):
        if self.items.size() == 0:
            return True
        return False

    def isFull(self):
        if self.items.size() == self.capacity:
            return True
        return False

    def push(self, item):
        if self.isFull():
            raise Exception("No capacity!")
        self.items.addLast(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("This Stack is Empty!")
        return self.items.deleteLast()

    def size(self):
        return self.items.size()

    def peek(self):
        if self.isEmpty():
            raise Exception("This Stack is Empty!")
        return self.items.rear.Book

