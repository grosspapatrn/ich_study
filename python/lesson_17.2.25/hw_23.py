print('Задание №1\n')

def generate_squares(n):
	for i in range(1, n+1):
		yield i * i

user_input = int(input('Введите число для получения квадрата: '))
squares = generate_squares(user_input)
print('\nВывод:\n')
for item in squares:
	print(item)


print('\n\nЗадание №2\n')

def fibonacci_generator():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b

user_input = int(input('Введите число: '))
print(f'\nВывод первых {user_input} чисел Фибоначчи:\n')
fibonacci = fibonacci_generator()
for number in range(user_input):
	print(next(fibonacci))





# fibonacci_gen = (x for x in range(1, int(input('Введите число Фибоначчи: ')) + 1))
# или
# user_input = int(input('Введите число: '))
# fibonacci_generator = (x for x in range(1, user_input + 1))
# print(f'\nВывод первых {user_input} чисел Фибоначчи:\n')
# a, b = 0, 1
# for i in fibonacci_generator:
# 	print(a, end='\n')
# 	a, b = b, a + b


# def fib(n):
# 	a, b = 0, 1
# 	for i in range(n):
# 		print(a, end=' ')
# 		a, b = b, a + b
#
# fib(10)