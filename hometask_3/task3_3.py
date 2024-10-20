inputList = [1, 2, 3, 4, 5, 6]

splitIndex = int(len(inputList) / 2) + int(len(inputList) % 2)

firstList = inputList[:splitIndex]
secondList = inputList[splitIndex:]

resultList = [firstList, secondList]
print(resultList)


