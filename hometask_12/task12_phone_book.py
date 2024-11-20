CONTINUE_PROGRAM = 'y'
PHONE_BOOK_FILE = 'phone_book.txt'

def start():
    while True:
        print('Enter "A" if you want to add contact\n'
              'Enter "F" if you want to find some contact\n'
              'Enter "R" if you want to remove contact\n'
              'Enter "C" if you want to remove contact\n')

        input_operation = str(input('What would you like to do?: '))

        match input_operation.lower():
            case "a":
                add_phone_number()
            case "f":
                find_by_name()
            case "r":
                remove_contact()
            case "c":
                change_contact()
            case _:
                print("Incorrect input")

        is_continue = input(f"Do you want to continue? \'{CONTINUE_PROGRAM}\' for yes: ")

        if is_continue.lower() != CONTINUE_PROGRAM:
            print("Exit from program...")
            break

def add_phone_number():
    input_name = str(input('Enter a name: '))
    input_number = int(input('Enter a number: '))

    with open(PHONE_BOOK_FILE, "a") as file:
        file.write(f"{input_name} - {input_number}\n")
        print(f"Contact {input_name} added")


def find_by_name():
    input_name = str(input('Enter a name to find in phone book: '))

    with open(PHONE_BOOK_FILE, "r") as my_file:
        result = my_file.readlines()

        for line in result:
            if input_name in line:
                print(f"Your contact: {line.strip()}")
                break
        else:
            print("Contact is not found.")


def change_contact():
    change_name = str(input('Enter a name of contact to change: '))
    change_number = 0
    match_found = False

    with open(PHONE_BOOK_FILE, "r") as file:
        lines = file.readlines()

        for line in lines:
            if change_name in line:
                match_found = True
                change_number = int(input('Enter changed phone number: '))

    if not match_found:
        print(f"The input '{change_name}' is not found in the phonebook.")
        return

    new_contact = f"{change_name} - {change_number}\n"

    for i in range(len(lines)):
        if change_name in lines[i]:
            lines[i] = new_contact

    with open(PHONE_BOOK_FILE, "w") as file:
        file.writelines(lines)
        print(f"Your changed contact: {new_contact}")

def remove_contact():
    input_name = str(input('Enter a name to remove from phone book: '))

    with open(PHONE_BOOK_FILE, "r") as my_file:
        lines = my_file.readlines()

    with open(PHONE_BOOK_FILE, "w") as file:
        for line in lines:
            if input_name not in line:
                file.write(line)

    print(f"Contact {input_name} has been removed.")

start()
