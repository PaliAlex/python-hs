inputList = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

secondList = []

for i in range(len(inputList)):
    if inputList[i] > 0:
        secondList.append(inputList[i])

for i in range(inputList.count(0)):
    secondList.append(0)

print(secondList)
