# my_list = [1, 2, 3]
# my_iterator = iter(my_list)
# print(next(my_iterator)) # 1
# print(next(my_iterator)) # 2
# print(next(my_iterator)) # 3

# numbers = iter(range(1, 1000001))
# print(2000 in numbers) # True
# print(2000 in numbers) # False

# import sys
# numbers = iter(range(1, 1000001))
# print(sys.getsizeof(numbers)) # 32
# numbers = range(1, 1000001)
# print(sys.getsizeof(numbers)) # 48

# my_list = [1, 2, 3]
# for item in my_list:
# 	print(item)

# iterator = iter(my_list)
# while True:
# 	try:
# 		print(next(iterator))
# 	except StopIteration:
# 		break

# def my_generator():
# 	yield 1
# 	yield 2
# 	yield 3
#
# gen = my_generator()
# print(next(gen)) # 1
# print(next(gen)) # 2
# print(next(gen)) # 3

# my_generator = (x for x in range(10))
# for x in my_generator:
# 	print(x) # 0 1 2 3 4 5 6 7 8 9
#
# my_generator = (x for x in range(10))
# my_list = list(my_generator)
# print(my_list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

import itertools

# my_list = [1, 2, 3, 4, 5]
# my_iterator = itertools.islice(my_list, 1, 4)
# for item in my_iterator:
# 	print(item) # 2 3 4

# colors = ['red', 'green', 'blue']
# sizes = ['S','M','L']
# for color, size in itertools.product(colors, sizes):
# 	print(color, size) # red S red M red L ...

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for item in itertools.chain(list1, list2):
	print(item) # 1 2 3 a b c
