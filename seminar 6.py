# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# ИСХОДНЫЙ КОД

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


# import os
# clear = lambda: os.system('cls')
# clear()
# import random


# def fill_list(arg_1: int):
#     new_list = [random.randint(0, 10) for index in range(arg_1)]
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

##############################################################################################################################################

# 3.Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# ИСХОДНЫЙ КОД

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
#     fractional_part = 0
#     fractional_part_list = []
#     result_of_difference = 0
#     for i in arg_1:
#         fractional_part = round(i - int(i), 2)
#         fractional_part_list.append(fractional_part)
#     print(f'Список дробых частей элементов: {fractional_part_list}')
    
#     max(fractional_part_list)
#     print(f'Максимальная дробная часть: {max(fractional_part_list)}')
#     min(fractional_part_list)
#     print(f'Минимальная дробная часть: {min(fractional_part_list)}')

#     result_of_difference = round(max(fractional_part_list) - min(fractional_part_list), 2)
#     return result_of_difference

# number = int(input('Задайте длину списка: '))
# filled_list = fill_list(number)
# print(f'Исходный список: {filled_list}')
# final_result = get_difference(filled_list)
# print(f'Разница между максимальным и минимальным значением дробной части элементов: {final_result}')


# import os
# clear = lambda: os.system('cls')
# clear()
# import random


# def fill_list(arg_1: int):
#     new_list = [round(random.uniform(0,5), 2) for i in range(arg_1) ]
#     return new_list


# def get_difference(arg_1: list):
#     result_of_difference = 0
#     fractional_part_list = [round(i - int(i), 2) for i in arg_1]
#     print(f'Список дробых частей элементов: {fractional_part_list}')
    
#     max(fractional_part_list)
#     print(f'Максимальная дробная часть: {max(fractional_part_list)}')
#     min(fractional_part_list)
#     print(f'Минимальная дробная часть: {min(fractional_part_list)}')

#     result_of_difference = round(max(fractional_part_list) - min(fractional_part_list), 2)
#     return result_of_difference

# number = int(input('Задайте длину списка: '))
# filled_list = fill_list(number)
# print(f'Исходный список: {filled_list}')
# final_result = get_difference(filled_list)
# print(f'Разница между максимальным и минимальным значением дробной части элементов: {final_result}')

########################################################################################################################################

# 5. Реализуйте алгоритм перемешивания списка.

# ИСХОДНЫЙ КОД

# import os
# clear = lambda: os.system('cls')
# clear()
# import random

# def fill_list(arg_1: int):
#     my_list = []
#     for index in range(arg_1):
#         my_list.append(random.randint(0, 30))
#     return my_list

# def shuffled_list(arg_1: list):
#     for i in range(len(arg_1)-1, 0, -1):
#         j = random.randint(0, i + 1)
#         arg_1[i], arg_1[j] = arg_1[j], arg_1[i]
#     print(f'Перемешанный список: {arg_1}')

# number = int(input('Задайте длину списка: '))
# filled_list = fill_list(number)
# print(f'Исходный список: {filled_list}')
# shuffled_list(filled_list)


# import os
# clear = lambda: os.system('cls')
# clear()
# import random


# def fill_list(arg_1: int):
#     my_list = [random.randint(0, 30) for index in range(arg_1)]
#     return my_list

# def shuffled_list(arg_1: list):
#     for i in range(len(arg_1)-1, 0, -1):
#         j = random.randint(0, i + 1)
#         arg_1[i], arg_1[j] = arg_1[j], arg_1[i]
#     print(f'Перемешанный список: {arg_1}')

# number = int(input('Задайте длину списка: '))
# filled_list = fill_list(number)
# print(f'Исходный список: {filled_list}')
# shuffled_list(filled_list)

################################################################################################################################

# 1.Напишите программу, удаляющую из текста все слова, содержащие "абв".

# ИСХОДНЫЙ КОД

# def delete_find_item(param_1: str):
#     list = []
#     for item in param_1:
#         if find_item not in item:
#             list.append(item)
#             result = " ".join(list)
#     return result


# text = 'абв голоабвдная муха селаабв на варенье'
# find_item = 'абв'
# splitted_text = text.split()
# final_result = delete_find_item(splitted_text)
# print(f'Исходный текст: {text}')
# print(f'Текст после удаления "{find_item}": {final_result}')


def delete_find_item(param_1: str):
    list = [item for item in param_1 if find_item not in item]
    result = " ".join(list)
    return result

text = 'абв голоабвдная муха селаабв на варенье'
find_item = 'абв'
splitted_text = text.split()
final_result = delete_find_item(splitted_text)
print(f'Исходный текст: {text}')
print(f'Текст после удаления "{find_item}": {final_result}')
