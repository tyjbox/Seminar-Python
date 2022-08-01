# 1.Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}


# import os
# clear = lambda: os.system('cls')
# clear()
# import math
# from math import pi

# def get_count(number: float):#  определяем количество знаков после запятой
#     number_conversion = str(number)
#     if '.' in number_conversion:
#         return abs(number_conversion.find('.') - len(number_conversion)) - 1
#     else:
#         return 0

# num_pi = pi
# print(f'Число Pi: {pi}')
# giv_accuracy = input('Введите точность, которую нужно определить, по образцу 0.001: ')
# accuracy_count = get_count(giv_accuracy)
# print(f'Число Pi c заданной точностью {giv_accuracy}: {round(math.pi, accuracy_count)}')

#2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# import os
# clear = lambda: os.system('cls')
# clear()

# num = int(input('Введите число: '))
# prime_fact_list = []
# fact = 2
# while num > 1:
#     if num % fact == 0:
#         prime_fact_list.append(fact)
#         num = num / fact
#     else:
#         fact += 1
# print(prime_fact_list)

#3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# import os
# clear = lambda: os.system('cls')
# clear()
# import random


# def fill_list(arg_1: int):
#     new_list = []
#     for index in range(arg_1):
#         new_list.append(random.randint(1, 6))
#     return new_list


# def non_repeating_elements(arg_1: list):
#     result_list = []
#     for i in arg_1:
#         if i not in result_list:
#             result_list.append(i)
#     return result_list

# num = int(input('Задайте длину списка: '))
# filled_list = fill_list(num)
# print(f'Исходный список: {filled_list}')
# final_result = non_repeating_elements(filled_list)
# print(f'Cписок неповторяющихся элементов: {final_result}')

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import os
clear = lambda: os.system('cls')
clear()
import random
deg_of_polynom = int(input("Введите степень: "))

def get_polynom(param_1: int):
    polynom = ""
    while param_1 >= 0:
        coeff = random.randint(0, 101)
        if coeff != 0:
            match param_1:
                case 1: polynom += (str(coeff) + "*x" + " + ")
                case 0: polynom += (str(coeff) + " = 0")
                case _: polynom += (str(coeff) + "*x^" + str(param_1) + " + ")
        param_1 -= 1
    return polynom

polynom_1 = get_polynom(deg_of_polynom)
print(f'Многочлен степени {deg_of_polynom}: {polynom_1}')

data = open('file_task_4.txt', 'w')
data.write(polynom_1)
data.close()