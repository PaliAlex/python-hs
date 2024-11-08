def add_one(some_list):
	number = ''
	result = []

	for i in some_list:
		number += str(i)

	number = int(number) + 1

	for i in str(number):
		result.append(int(i))

	return result


print(add_one([1, 2, 3, 4]))
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
