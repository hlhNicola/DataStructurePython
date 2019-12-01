from assignment_2 import DLinkedListADT

class QueueADT:

    def __init__(self, min):
        if min <= 0:
            raise Exception("No capacity!")
        self.items = DLinkedListADT.DlinkedListADT()
        self.capacity = min * 2

    def sEmpty(self):
        if self.items.size() == 0:
            return True
        return False

    def isFull(self):
        if self.items.size() == self.capacity:
            return True
        return False

    def enQueue(self, item):
        if self.isFull():
            raise Exception("No capacity!")
        self.items.addLast(item)

    def deQueue(self):
        if self.isEmpty():
            raise Exception("This Stack is Empty!")
        self.items.deleteFirst()

    def size(self):
        return self.items.size()
