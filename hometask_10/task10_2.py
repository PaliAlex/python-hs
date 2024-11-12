import re

def first_word(text):
    match = re.search(r"^\W*([A-Za-z]+(?:'[A-Za-z]+)?)", text)

    return match.group(1)


print(first_word("Hello.World"))

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')