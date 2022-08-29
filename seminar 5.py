# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

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

# 2. Задание не готово!!((


# 3.Создайте программу для игры в ""Крестики-нолики"".(код команды)


# import random
# import os

# enemy_variations= []
# variations = []

# def enemy_turn():

#     while True:
#         num = random.randint(0,8)
#         if cell[num] == '':
#             cell[num] = 'O'

#             # os.system('cls' if os.name == 'nt' else 'clear')
#             print(f'{cell[0]:^5}|{cell[1]:^5}|{cell[2]:^5}')
#             print(f'-----------------')
#             print(f'{cell[3]:^5}|{cell[4]:^5}|{cell[5]:^5}')
#             print(f'-----------------')
#             print(f'{cell[6]:^5}|{cell[7]:^5}|{cell[8]:^5}')
#             lenn = len(user_turns)
#             if lenn >= 3:
#                 enemy_variations = [(i, j, k) for i in user_turns for j in user_turns for k in user_turns]
#             return




# cell = ['' for x in range(9)]
# print(f'{cell[0]:^5}|{cell[1]:^5}|{cell[2]:^5}')
# print(f'-----------------')
# print(f'{cell[3]:^5}|{cell[4]:^5}|{cell[5]:^5}')
# print(f'-----------------')
# print(f'{cell[6]:^5}|{cell[7]:^5}|{cell[8]:^5}')
# turn = 0

# win_combinations = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

# user_turns = []
# game = True
# while game:
#     while True:
#         number = int(input('Введите ячейку: '))
#         if cell[number] == '':
#             cell[number] = 'X'
#             break
#     user_turns.append(number)
#     # os.system('cls' if os.name == 'nt' else 'clear')
#     print(f'{cell[0]:^5}|{cell[1]:^5}|{cell[2]:^5}')
#     print(f'-----------------')
#     print(f'{cell[3]:^5}|{cell[4]:^5}|{cell[5]:^5}')
#     print(f'-----------------')
#     print(f'{cell[6]:^5}|{cell[7]:^5}|{cell[8]:^5}')
#     print(user_turns)
#     lenn = len(user_turns)
#     if lenn >= 3:
#         variations = [(i, j ,k) for i in user_turns for j in user_turns for k in user_turns]

#     for elemnt in variations:
#         if elemnt in win_combinations:
#             print('Победа')
#             game = False
#     if game: enemy_turn()
#     turn += 1


# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# (Кодирование длины выполнения (RLE)

# создаем входные данные в отдельном текстовом файле

# with open('RLE_1.txt', 'w') as file:
#     file.write('qqqrrrrggggvcv')
#     file.close()

# считываем нашу строку из первого файла

# with open('RLE_1.txt', 'r') as data:
#     rle_1_string = data.read()

# # модуль сжатия 

# def encode_the_string(param_1: str):
#     new_string_encoding = ''
#     previous_char = ''
#     counter = 1
#     if not param_1: return ''
#     for current_char in param_1:
#         if current_char != previous_char:
#             if previous_char:
#                 new_string_encoding += str(counter) + previous_char
#             counter = 1
#             previous_char = current_char
#         else: 
#             counter += 1
#     else:
#         new_string_encoding += str(counter) + previous_char
#     return new_string_encoding


# encoded_string = encode_the_string(rle_1_string)
# print(f'Сжатые данные: {encoded_string}')

# # записываем сжатые данные во второй файл

# with open('RLE_2.txt', 'w') as file:
#     file.write(encoded_string)
#     file.close()


# # считываем нашу строку из второго файла для декодинга

# with open('RLE_2.txt', 'r') as data:
#     rle_2_string = data.read() 
#     file.close()

# # модуль восстановления

# def decode_the_string(param_1: str):
#     new_string_decoding = ''
#     counter_string = ''
#     for char in param_1:
#         if char.isdigit():
#             counter_string += char
#         else:
#             new_string_decoding += char * int(counter_string)
#             counter_string = ''
#     return new_string_decoding

# decoded_string = decode_the_string(rle_2_string)
# print(f'Восстановленные данные: {decoded_string}')