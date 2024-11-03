def correct_sentence(text):
    sentence_list = text.split('.')
    result = ''

    for item in sentence_list:
        if item == '': break

        item = item.strip().capitalize()
        result = result + item + '. '

    return result.strip()


print(correct_sentence('Greetings. Friends'))
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')