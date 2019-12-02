# Lihong
# solution of stack2
# result should be ["B", "E", "D", "C", "G", "F", "A"] after correct operations

initialStack = []
resultSequence = []

initialStack.append("A")
initialStack.append("B")
resultSequence.append(initialStack.pop())
initialStack.append("C")
initialStack.append("D")
initialStack.append("E")
resultSequence.append(initialStack.pop())
resultSequence.append(initialStack.pop())
resultSequence.append(initialStack.pop())
initialStack.append("F")
initialStack.append("G")
resultSequence.append(initialStack.pop())
resultSequence.append(initialStack.pop())
resultSequence.append(initialStack.pop())

print("AB*CDE***FG***:", resultSequence)

