inputList = [12, 3, 4, 10, 8]

if not len(inputList) == 0:
    lastElement = inputList.pop(len(inputList) - 1)
    inputList.insert(0, lastElement)

print(inputList)

