def common_elements():
	multiples_of_three = set()
	multiples_of_five = set()

	for index in range(100):
		if index % 3 == 0:
			multiples_of_three.add(index)

		if index % 5 == 0:
			multiples_of_five.add(index)

	return multiples_of_five & multiples_of_three

common_elements()
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

