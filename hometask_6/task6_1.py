import string

all_letters = string.ascii_letters

input_text = input('Enter letters range: ')
letters = input_text.split('-')

start_range_index = all_letters.index(letters[0])
end_range_index = all_letters.index(letters[1])+1

print(all_letters[start_range_index:end_range_index])
