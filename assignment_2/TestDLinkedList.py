from assignment_2 import Book

HarryPotter = Book.Book('0001', 250, 'Harry Potter')
GameOfThrone = Book.Book('0002', 1200, 'GameOfThrone')
TheThreeBodyProblem = Book.Book('0003', 1500, 'TheThreeBodyProblem')

WrongPagesGameOfThrone = Book.Book('0002', '1200', 'GameOfThrone')
WrongIsbnGameOfThrone = Book.Book('0000000000000000002', '1200', 'GameOfThrone')
WrongTitleGameOfThrone = Book.Book('0002', '1200', True)

# HarryPotter.bookValidation()
# GameOfThrone.bookValidation()
# TheThreeBodyProblem.bookValidation()
# WrongPagesGameOfThrone.bookValidation()
# WrongIsbnGameOfThrone.bookValidation()
# WrongTitleGameOfThrone.bookValidation()

