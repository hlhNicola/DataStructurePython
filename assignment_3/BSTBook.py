# Lihong
# implementation of BST class and related operations

class Node:
    def __init__(self, initdata):
        self.Book = initdata
        self.left = None
        self.right = None

    def getKey(self):
        return self.Book.getKey()

    def getAuthor(self):
        return self.Book.getAuthor()

class BST:
    def __init__(self, data):
        self.root = Node(data)
        return

    def find(self, key):
        return self.findR(self.root, key)

    def findR(self, root, key):
        if root is None:
            return None
        if root.getKey() == key:
            return root
        if key > root.getKey():
            return self.findR(root.right, key)
        if key < root.getKey():
            return self.findR(root.left, key)


    def insert(self, data):
        self.root = self.insertR(self.root, data)

    def insertR(self, root, data):
        newNode = Node(data)
        if root is None:
            root = newNode
        if newNode.getKey() < root.getKey():
            root.left = self.insertR(root.left, data)
        if newNode.getKey() > root.getKey():
            root.right = self.insertR(root.right, data)
        return root

    def printBooks(self):
        self.printBooksR(self.root)


    def printBooksR(self, root):
        if root is not None:
            self.printBooksR(root.left)
            print('ISBN:', root.getKey())
            self.printBooksR(root.right)

    def printAuthor(self, name):
        self.printAuthorR(self.root, name)

    def printAuthorR(self, root, name):
        if root is not None:
            if root.getAuthor() == name:
                print('ISBN:', root.getKey(), 'is writen by', name)
            self.printAuthorR(root.left, name)
            self.printAuthorR(root.right, name)

