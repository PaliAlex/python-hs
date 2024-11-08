def is_palindrome(text):
    filtered_symbols = []

    for letter in text:
       if letter.isalpha() or letter.isdigit():
           filtered_symbols.append(letter.lower())

    refactored_text = ''.join(filtered_symbols)
    text_to_compare = refactored_text[::-1]

    return refactored_text == text_to_compare

print(is_palindrome('0P'))

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
