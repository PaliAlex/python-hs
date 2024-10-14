inputNumber = int(input('Enter a five-digit number : '))

firstNumber = inputNumber // 10000
secondNumber = inputNumber // 1000 % 10
thirdNumber = inputNumber // 100 % 10
fourthNumber = inputNumber // 10 % 10
fifthNumber = inputNumber % 10

print(f'Input number: {inputNumber}')
print(f'Reverted number: {fifthNumber}{fourthNumber}{thirdNumber}{secondNumber}{firstNumber}')
