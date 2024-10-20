inputList = []

splitIndex = int(len(inputList) / 2) + int(len(inputList) % 2)

firstList = inputList[:splitIndex]
secondList = inputList[splitIndex:]

resultList = [firstList, secondList]
print(resultList)


