inputNumber = int(input('Enter a four-digit number : '))

print(f'First number: {inputNumber // 1000}')
print(f'Second number: {inputNumber // 100 % 10}')
print(f'Third number: {inputNumber // 10 % 10}')
print(f'Fourth number: {inputNumber % 10}')