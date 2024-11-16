def is_even(number):
    ok_values = list(range(0, 10, 2))

    to_string = str(number)
    last_char = to_string[-1]

    return int(last_char) in ok_values

print(is_even(1056897**2))

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('OK')
