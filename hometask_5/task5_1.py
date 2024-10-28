import keyword
import string

punctuationSigns = string.punctuation
reservedWords = keyword.kwlist

isValidName = 'True'

inputVariableName = input('Input variable name: ')

if inputVariableName.count("__") > 0:
    isValidName = 'False'
    print("Error! Variable can't have more than one underscore in a row.")

if not inputVariableName[0].isnumeric():
    for symbolInName in inputVariableName:
        if symbolInName.isupper():
            isValidName = 'False'
            print(f'Error! Symbols in upper case are forbidden')

        if symbolInName == ' ':
            isValidName = 'False'
            print(f'Error! Spaces are forbidden.')

        for sign in punctuationSigns:
            if symbolInName == sign and symbolInName != '_':
                isValidName = 'False'
                print(f'Error! Symbol {symbolInName} is forbidden.')
                break
else:
    isValidName = 'False'
    print(f"Error! Variable can't start from number")

for word in reservedWords:
    if word.lower() == inputVariableName.lower():
        isValidName = 'False'
        print(f"Error! '{inputVariableName}' is a reserved word.")

print(isValidName)