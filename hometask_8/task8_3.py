def find_unique_value(some_list):
    unique_numbers_list = list(set(some_list))
    unique_values = []

    for number in unique_numbers_list:
        if some_list.count(number) == 1:
            unique_values.append(number)

    return unique_values[0]

print(find_unique_value([5, 5, 5, 2, 2, 0.5]))

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
