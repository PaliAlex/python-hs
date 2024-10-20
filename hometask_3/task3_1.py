firstParameter = int(input('Enter a first number : '))
action = input('Enter an action : ')
secondParameter = int(input('Enter a second number : '))

match action:
    case "+":
        print(f'The answer is {firstParameter + secondParameter}')
    case "-":
        print(f'The answer is {firstParameter - secondParameter}')
    case "*":
        print(f'The answer is {firstParameter * secondParameter}')
    case "/":
        if secondParameter == 0:
            print('Second parameter cannot be 0.')
        else:
            print(f'The answer is {int(firstParameter / secondParameter)}')
    case _:
        print("Invalid action please try again")