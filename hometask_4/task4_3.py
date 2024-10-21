import random

numbers = []
for i in range(random.randint(3,10)):
    numbers.append(random.randint(1,10))

answer = [
    numbers[0],
    numbers[2],
    numbers[-2]
]

print(f'The list is: {numbers}')
print(f'The answer is: {answer}')
