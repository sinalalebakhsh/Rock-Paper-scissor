import os
os.system('cls')
import random

dict_all = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissor',
    }

user_choice = ''

first_round_game = 0
final_round_game = 5



print('for finish, write finish\n')

while first_round_game != final_round_game:

    while user_choice != 'finish':
        ai_choice = random.choice(list(dict_all.values()))
        user_choice = input('rock | paper | scissor ?')
        if user_choice == 'finish':
            first_round_game = final_round_game
            break
        user_choice = user_choice.lower()
        if user_choice in dict_all.keys():
            if user_choice == 'r':
                user_choice = 'rock'
            elif user_choice == 'p':
                user_choice = 'paper'
            else:
                user_choice = 'scissor'
        if user_choice in dict_all.keys() or user_choice in dict_all.values() :
            if user_choice == ai_choice:
                print(f'Equal match. you = {user_choice} || main = {ai_choice}')
            elif (user_choice == 'r' or user_choice == 'rock') and ai_choice == 'scissor':
                print(f'You Won. you = {user_choice} || main = {ai_choice}')
            elif (user_choice == 'p' or user_choice == 'paper') and ai_choice == 'rock':
                print(f'You Won. you = {user_choice} || main = {ai_choice}')
            elif (user_choice == 's' or user_choice == 'scissor') and ai_choice == 'paper':
                print(f'You Won. you = {user_choice} || main = {ai_choice}')
            else:
                print(f'You LOST. you = {user_choice} || main = {ai_choice}')
            
        elif user_choice != dict_all.keys() and user_choice != dict_all.values() and user_choice != 'finish':
            print('write r/p/s or rock | paper | scissor ')
            first_round_game -= 1 
        first_round_game += 1
        if first_round_game == final_round_game:
            break
    
        












#This was my previous attempt. Maybe it will help you
#This was my previous attempt. Maybe it will help you
#This was my previous attempt. Maybe it will help you
#This was my previous attempt. Maybe it will help you


# dict_r = {'r':'rock'}
# dict_p = {'p':'paper'}
# dict_s = {'s':'scissor'}
# user_choice = ''

# while user_choice != 'finish':
#     ai_choice = random.choice([ {'r':'rock'} , {'p':'paper'} , {'s':'scissor'} ])
#     user_choice = input('rock , paper , scissor ?')
#     if user_choice in dict_all.keys() or user_choice in dict_all.values():
#         if (user_choice in dict_r.keys() or user_choice in dict_r.values()) and ai_choice == dict_s:
#             print('congratulations. You won. your choice is Rock & main is Scissor.')
#         elif (user_choice in dict_p.keys() or user_choice in dict_p.values()) and ai_choice == dict_r:
#             print('congratulations. You won. your choice is Paper & main is Rock.')
#         elif (user_choice in dict_s.keys() or user_choice in dict_s.values()) and ai_choice == dict_p:
#             print('congratulations. You won. your choice is rock & main is scissor.')
#         elif (user_choice in dict_r.keys() or user_choice in dict_r.values()) and ai_choice ==dict_p:
#             print(' YOU ARE LOST :( your Rock and main Paper')
#         elif (user_choice in dict_p.keys() or user_choice in dict_p.values()) and ai_choice ==dict_s:
#             print(' YOU ARE LOST :( your Paper and main Scissor')
#         elif (user_choice in dict_s.keys() or user_choice in dict_s.values()) and ai_choice ==dict_r:
#             print(' YOU ARE LOST :( your Scissor and main Rock')
#         else:
#             print('cant empty')
#     else:
#         print('Your Choice just can be r | p | s or Rock , Paper , Scissor ')
    

    




