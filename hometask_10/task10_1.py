from inspect import isgenerator

def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    current_value = begin

    for i in range(end):
        yield current_value
        current_value = func(current_value)

gen = some_gen(2, 4, pow)

def get_list(generator):
    list_list = []

    for i in generator:
        list_list.append(i)

    return list_list

assert isgenerator(gen) == True, 'Test1'
assert get_list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')