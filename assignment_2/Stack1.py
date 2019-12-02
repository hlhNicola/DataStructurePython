# Lihong
# solution of stack1

initialStack = []
resultSequence = []

initialStack.append("A")
resultSequence.append(initialStack.pop())
initialStack.append("B")
initialStack.append("C")
resultSequence.append(initialStack.pop())
initialStack.append("E")
initialStack.append("F")
resultSequence.append(initialStack.pop())
resultSequence.append(initialStack.pop())
initialStack.append("G")
resultSequence.append(initialStack.pop())
initialStack.append("H")
resultSequence.append(initialStack.pop())
resultSequence.append(initialStack.pop())

print("A*BC*EF**G*H**:", resultSequence)
