from inspect import isgenerator

def is_prime(n):
    divisors = []

    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            divisors.append(i)

    return len(divisors) == 0

def prime_generator(end):
    for i in range(end + 1):
        if is_prime(i):
            yield i

gen = prime_generator(31)

def get_list(generator):
    list_list = []

    for i in generator:
        list_list.append(i)

    return list_list

print(get_list(gen))

assert isgenerator(gen) == True, 'Test0'
assert get_list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert get_list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert get_list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
