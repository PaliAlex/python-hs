from inspect import isgenerator

def calculate_cube(x):
    return x ** 3

def generate_cube_numbers(end):
    for i in range(2, end):
        if calculate_cube(i) <= end:
            yield calculate_cube(i)

def get_list(generator):
    list_list = []

    for i in generator:
        list_list.append(i)

    return list_list

gen = generate_cube_numbers(1000)

print(get_list(gen))

assert isgenerator(gen) == True, 'Test0'
assert get_list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert get_list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert get_list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
