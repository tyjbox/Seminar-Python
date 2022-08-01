# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import os
# clear = lambda: os.system('cls')
# clear()
# import random

# def fill_list(arg_1: int):
#     new_list = []
#     for index in range(arg_1):
#         new_list.append(random.randint(0, 10))
#     return new_list


# def elements_summ(arg_1: list):
#     summ = 0
#     i = 0    
#     for i in range(1, len(arg_1), 2):
#        summ += arg_1[i]
#        i += 1
#     return summ        

# number = int(input('Задайте длину списка: '))
# filled_list = fill_list(number)
# print(f'Исходный список: {filled_list}')
# final_result = elements_summ(filled_list)
# print(f'Сумма элементов списка, стоящих на нечётной позиции: {final_result}')


#2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

# import os
# clear = lambda: os.system('cls')
# clear()
# import random

# def fill_list(arg_1: int):
#     new_list = []
#     for index in range(arg_1):
#         new_list.append(random.randint(0, 10))
#     return new_list


# def elements_multiplicaton(param_1: list):
#     i = 0
#     j = len(param_1) - 1
#     result = []
#     while i < len(param_1) / 2:
#         result.append(param_1[i] * param_1[j])
#         i += 1
#         j -= 1
#     return result


# num = int(input('Задайте длину списка: '))
# filled_list = fill_list(num)
# print(f'Исходный список: {filled_list}')
# new_list = []
# new_list = elements_multiplicaton(filled_list)
# print(f'Произведение пар чисел исходного списка: {new_list}')

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import os
# clear = lambda: os.system('cls')
# clear()
# import random

# def fill_list(arg_1: int):
#     new_list = []
#     for i in range(arg_1):
#         new_list.append(round(random.uniform(0,5), 2))
#     return new_list


# def get_difference(arg_1: list):
#     fract_part = 0
#     fract_part_list = []
#     result_of_diff = 0
#     for i in arg_1:
#         fract_part = round(i - int(i), 2)
#         fract_part_list.append(fract_part)
#     print(f'Список дробых частей элементов: {fract_part_list}')
    
#     max(fract_part_list)
#     print(f'Максимальная дробная часть: {max(fract_part_list)}')
#     min(fract_part_list)
#     print(f'Минимальная дробная часть: {min(fract_part_list)}')

#     result_of_diff = round(max(fract_part_list) - min(fract_part_list), 2)
#     return result_of_diff

# num = int(input('Задайте длину списка: '))
# filled_list = fill_list(num)
# print(f'Исходный список: {filled_list}')
# final_result = get_difference(filled_list)
# print(f'Разница между максимальным и минимальным значением дробной части элементов: {final_result}')


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# import os
# clear = lambda: os.system('cls')
# clear()
# import random

# def get_binary_number(param_1: int):
#     result = ' '
#     while param_1 > 0:
#         result += str(param_1 % 2)
#         param_1 = param_1 // 2
#     return result[::-1]

# number = int(input('Введите десятичное число: '))
# final_result = get_binary_number(number)
# print(f'Десятичное число {number} в двоичной системе счисления равно: {final_result}')


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


# import os
# clear = lambda: os.system('cls')
# clear()
# import random

# def get_fib_num(param_1: int):
#     fib_list = []
#     fib_num_1 = 1
#     fib_num_2 = 1
#     for i in range(param_1):
#         fib_list.append(fib_num_1)
#         fib_num_1, fib_num_2 = fib_num_2, fib_num_1 + fib_num_2

#     fib_num_1 = 0
#     fib_num_2 = 1
#     for i in range(param_1 + 1):
#         fib_list.insert(0,fib_num_1)
#         fib_num_1, fib_num_2 = fib_num_2, fib_num_1 - fib_num_2        
       
#     return fib_list

# num = int(input('Введите число: '))
# final_list = get_fib_num(num)
# print(f'Cписок чисел Фибоначчи: {final_list}')