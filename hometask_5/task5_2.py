CONTINUE_PROGRAM_USER_SELECT = 'y'

while True:
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

    is_continue = input(f"Do you want to continue? \'{CONTINUE_PROGRAM_USER_SELECT}\' for yes: ")

    if is_continue != CONTINUE_PROGRAM_USER_SELECT:
        print("Exit from program...")
        break
