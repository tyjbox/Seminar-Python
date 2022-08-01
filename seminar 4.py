#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#Пример:

#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
clear = lambda: os.system('cls')
clear()
import random

def fill_list(arg_1: int):
    new_list = []
    for i in range(arg_1):
        new_list.append(round(random.uniform(0,5), 2))
    return new_list


def get_difference(arg_1: list):
    fractional_part = 0
    fractional_part_list = []
    result_of_difference = 0
    for i in arg_1:
        fractional_part = round(i - int(i), 2)
        fractional_part_list.append(fractional_part)
    print(f'Список дробых частей элементов: {fractional_part_list}')
    
    max(fractional_part_list)
    print(f'Максимальная дробная часть: {max(fractional_part_list)}')
    min(fractional_part_list)
    print(f'Минимальная дробная часть: {min(fractional_part_list)}')

    result_of_difference = round(max(fractional_part_list) - min(fractional_part_list), 2)
    return result_of_difference

number = int(input('Задайте длину списка: '))
filled_list = fill_list(number)
print(f'Исходный список: {filled_list}')
final_result = get_difference(filled_list)
print(f'Разница между максимальным и минимальным значением дробной части элементов: {final_result}')
