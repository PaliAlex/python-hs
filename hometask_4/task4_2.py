inputList = [0, 1, 7, 2, 4, 8]

evenIndexesList = inputList[::2]

total = 0

for i in range(len(evenIndexesList)):
    total += evenIndexesList[i]

if not len(inputList) == 0:
    answer = total * inputList[len(inputList)-1]
    print(answer)
else:
    print(0)



