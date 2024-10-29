input_number = str(input('Enter a number: '))
result = 1
number_list = []

# Створюємо список з інпут намбера
for number in input_number:
    number_list.append(number)

while True:
    currentResult = 1

    # Цикл перемноження елементів списку
    for num in number_list:
        currentResult = currentResult * int(num)

    # Присвоюємо глобальному значенню результату поточний і обнуляємо його, чистимо список
    result = currentResult
    currentResult = 1
    number_list.clear()

    # З оновленого глобального результату створюємо список
    for number in str(result):
        number_list.append(number)

    if result <= 9:
        break

print(f'The answer is {result}')
