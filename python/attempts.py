# while True:
#
#     string_input = input("Enter a string: ").lower().replace(' ', '')
#     start = 97
#     end = 122
#     while start < end:
#         is_found = chr(start)               # изменение числа в символ
#         temp = is_found in string_input     # временный поиск символа в строке
#         if not temp:
#             print(f'is false.')
#             break
#         start += 1
#     if start == end:
#         print(f'is true.')
#
#     exit = False
#
#     while not exit:
#         if exit:
#             break
#         ask = input(f'do you want to continue? y/n ').lower()
#         if ask == 'n':
#             exit = True
#             break
#         if ask == 'y':
#             exit = False
#             break
#         else:
#             print(f'type error.')
#
#     if exit:
#         print(f'closing program.')
#         break
#     else:
#         continue

# bcdfghjklmnpqrstvwxz

"""
# print(f'\nЗадание №2')
#
# user_input = input(f'\nВведите строку: ').lower().replace(' ', '')
# vowels = ['a', 'e', 'i', 'o', 'u']
# consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
#
# vowels_count = []
# consonant_count = []
#
# for v in user_input:
#     if v in vowels:
#         vowels_count.insert(0, v)
# for c in user_input:
#     if c in consonants:
#         consonant_count.insert(0, c)
#
# vowels_len = len(vowels_count)
# consonant_len = len(consonant_count)
#
# print(f'\nКоличество гласных букв: {vowels_len}')
# print(f'Количество согласных букв: {consonant_len}')
"""

"""
user_input = input(f'Введите строку на английском: ')
dublicates = ""
check = ""
count = 0

while count < len(user_input):
    if user_input[count] in check:
        if user_input[count] not in dublicates:
            dublicates += user_input[count]
    else:
        check += user_input[count]
    count += 1
if dublicates == '':
    print(f'Все символы в строке уникальны.')
else:
    print(f'Символы \"{", ".join(dublicates)}\" повторяются.')
    """

"""
total_age = 0
count_man = 0
count_woman = 0
average_age_male = 0
average_age_female = 0
exit = False

while True:
    name = input(f'Введите ваше имя: ')
    last_name = input(f'Введите вашу фамилию: ')
    gender = input(f'Введите ваш пол (m/f): ')
    while gender != 'm' and gender != 'f':
        err = input(f'Ошибка. Введите \'m\' или \'f\': ')
        if err == 'm':
            gender = 'm'
            break
        elif err == 'f':
            gender = 'f'
            break
    age = int(input(f'Введите ваш возраст: '))
    print(f'Hello, {name} {last_name}!')
    if gender == 'm':
        total_age += age
        count_man += 1
        average_age_male = total_age / count_man
        # print(f'Средний возраст всех мужчин: {average_age:.1f}')
    elif gender == 'f':
        total_age += age
        count_woman += 1
        average_age_female = total_age / count_woman
        # print(f'Средний возраст всех женщин: {average_age:.1f}')

    while not exit:
        if exit:
            break
        ask = input(f'Хотите продолжить (+/-)? ')
        if ask == '-':
            exit = True
            break
        elif ask == '+':
            exit = False
            break
        else:
            print(f'Ошибка ввода.')

    if exit:
        print(f'Средний возраст всех мужчин: {average_age_male:.1f}')
        print(f'Средний возраст всех женщин: {average_age_female:.1f}')
        break
    else:
        continue
"""


"""print(f'\nЗадание №2', f'\n')

user_output = []


def is_float(x):
    return isinstance(x, float)


while True:
    user_input = input(f'Введите число или слово "Выход" / "Exit" для завершения: ').capitalize()

    if user_input == "Выход" or user_input == "Exit":
        print(f'\nДинамический массив: {user_output}')
        break

    # elif isinstance(user_input, float):
    #     user_input = float(user_input)

    elif is_float(user_input):
        user_input = int(user_input)
        user_input = float(user_input)

    elif user_input.isalpha():
        while user_input.isalpha():
            err_input = input(f'\nОшибка ввода. \nВведите число: ')
            if err_input.isdigit():
                user_input = int(err_input)
                break

    # elif user_input.isalnum() == False or user_input.isdigit() == False:
    #     while user_input.isalnum() == False or user_input.isdigit() == False:
    #         err_input = input(f'\nОшибка ввода. \nВведите число: ')
    #         if err_input.isdigit():
    #             user_input = int(err_input)
    #             break

    elif user_input.isdigit():
        user_input = int(user_input)

    user_output.append(user_input)




# x = 42.0  # главный ответ всегда 42
# is_int = isinstance(x, int)  # False, потому что это вещественное число
# is_float = isinstance(x, float)  # True, так как число вещественное
# print(is_int, is_float)"""










# print(f'\nЗадание №2', f'\n')
#
# user_output = []
#
# while True:
#     user_input = input(f'Введите число или слово "Выход" / "Exit" для завершения: ').capitalize()
#
#     if user_input == "Выход" or user_input == "Exit":
#         print(f'\nДинамический массив: {user_output}')
#         break
#
#     elif user_input.isdecimal() == False:
#         user_input = float(user_input)
#
#     elif user_input.isdigit() == True:
#         user_input = int(user_input)
#
#     user_output.append(user_input)






# user_output = []
#
#
# def is_float(value):
#     try:
#         float(value)  # Попытка преобразовать строку в float
#         return True
#     except ValueError:
#         return False
#
#
# while True:
#     user_input = input(f'Введите число или слово "Выход" / "Exit" для завершения: ').capitalize()
#
#     if user_input == "Выход" or user_input == "Exit":
#         print(f'\nДинамический массив: {user_output}')
#         break
#
#     elif is_float(user_input):
#         user_input = int(user_input)
#         user_input = float(user_input)
#
#     elif user_input.isalpha():
#         while user_input.isalpha():
#             err_input = input(f'\nОшибка ввода. \nВведите число: ')
#             if err_input.isdigit():
#                 user_input = int(err_input)
#                 break
#
#     elif user_input.isdigit():
#         user_input = int(user_input)
#
#     user_output.append(user_input)






# user_output = [] # создание пустого списка
#
# while True:
#     user_input = input(f'Введите число или слово "Выход" / "Exit" для завершения: ').capitalize()
#
#     # создание условия для выхода из программы
#     if user_input == "Выход" or user_input == "Exit":
#         print(f'\nДинамический массив: {user_output} ')
#         break
#
#     # проверка ввода на наличие букв с циклом повтора ввода
#     elif user_input.isalpha():
#         while user_input.isalpha():
#             err_input = input(f'\nОшибка ввода. \nВведите число: ')
#             if err_input.isdigit():
#                 user_input = int(err_input)
#                 break
#
#     # проверка ввода на отсутствие букв или цифр с циклом повтора ввода
#     elif user_input.isalnum() == False or user_input.isdigit() == False:
#         while user_input.isalnum() == False or user_input.isdigit() == False:
#             err_input = input(f'\nОшибка ввода. \nВведите число: ')
#             if err_input.isdigit():
#                 user_input = int(err_input)
#                 break
#
#     # проверка ввода на наличие цифр
#     elif user_input.isdigit():
#         user_input = int(user_input)
#
#     # добавление новых значений в существующий список
#     user_output.append(user_input)
#
#
# print(f'Сумма ваших чисел равна {sum(user_output)}')
#
# result = 1
# for num in user_output:
#     result *= num
#
# print(f'Произведение ваших чисел равно {result}')
# print(user_output[::-1])
#
#
#
#
#
# us_inp = input(f'Введите числа через пробел: ')
# us_list = list(us_inp)
# print(f'Сумма ваших чисел равна {sum(us_inp)}')




# bro = 12345
#
# def sum_digits(n):
#     if n < 10:
#         return n
#     else:
#         pass
#     return n%10 + sum_digits(n//10)
#
# print(sum_digits(bro))