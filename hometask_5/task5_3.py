import string

input_text = "i like python community!"

punctuation_signs = string.punctuation

words_list = input_text.split(' ')

new_list = []

for word in words_list:
    word = word.capitalize()

    for symbol in word:
        if symbol in punctuation_signs:
            word = word.replace(symbol, '')

    new_list.append(word)

print("#" + "".join(new_list))