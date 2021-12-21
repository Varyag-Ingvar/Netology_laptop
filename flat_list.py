nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)

# for i in flat_list:
# 	print(i)


