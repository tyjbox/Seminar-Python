# 1. Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

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

