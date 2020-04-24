# import csv
# from answers import get_number_answers
# from pathlib import Path
from display import display_current_question, display_round
from time import sleep
from colored import fg, attr
import os
from random import randint
from players import retreive_winning_player
from pathlib import Path
from display import display_answers_in
random_block = '░'

colors = [87, 158, 216, 187, 225, 169, 141, 147]

random_color = fg(colors[randint(0,len(colors)-1)])

# data_path = str(Path(__file__).parent)+'\\Data\\'
# temp_file = data_path + 'temp.txt'
# answers_file = data_path + 'answers.csv'
# players_file = data_path + 'players.csv'
# questions_file = data_path + 'game_of_things_questions.txt'

animation = {
    'static1': 
    '\n' * 3,

    'static2': 
    '\n',

    'movement1': 
    '\n' * 2 +
    ' ' * 21 + random_block * 20 + '\n' +
    ' ' * 18 + random_block * 3 + ' ' * 20 + random_block + '\n' +
    ' ' * 16 + random_block * 2 + ' ' * 24 + random_block * 2 + '\n' +
    ' ' * 15 + random_block + ' ' * 28 + random_block + '\n' +
    ' ' * 14 + random_block + ' ' * 30 + random_block + '\n' +
    ' ' * 13 + random_block + ' ' * 7 + random_block + ' ' * 24 + random_block + '\n' +
    ' ' * 12 + random_block + ' ' * 28 + random_block + ' ' * 5 + random_block + '\n' +
    ' ' * 11 + random_block + ' ' * 35 + random_block + '\n' +
    ' ' * 11 + random_block + ' ' * 13 + random_block * 14 + ' ' * 9 + random_block + '\n' +
    ' ' * 11 + random_block + ' ' * 36 + random_block + '\n' +
    ' ' * 12 + random_block * 36,

    'movement2': 
    ' ' * 20 + random_block * 22 + '\n' +
    ' ' * 17 + random_block * 3 + ' ' * 22 + random_block * 3 + '\n' +
    ' ' * 15 + random_block * 2 + ' ' * 28 + random_block * 2 + '\n' +
    ' ' * 14 + random_block + ' ' * 32 + random_block + '\n' +    
    ' ' * 13 + random_block + ' ' * 34 + random_block + '\n' +
    ' ' * 12 + random_block + ' ' * 7 + random_block + ' ' * 28 + random_block + '\n' +
    ' ' * 11 + random_block + ' ' * 28 + random_block + ' ' * 8 + random_block + '\n' +
    ' ' * 11 + random_block + ' ' * 37 + random_block + '\n' +
    ' ' * 12 + random_block + ' ' * 35 + random_block + '\n' +
    ' ' * 12 + random_block + ' ' * 11 + random_block * 14 + ' ' * 10 + random_block + '\n' +
    ' ' * 13 + random_block * 2 + ' ' * 31 + random_block * 2 + '\n' +
    ' ' * 15 + random_block + ' ' * 29 + random_block + '\n' +
    ' ' * 16 + random_block * 29 + '\n'
    }


# while True:
#     os.system('cls')
#     print(animation['static1'])
#     print(animation['movement1'])
#     print(animation['static2'])
#     sleep(.3)
#     os.system('cls')
#     print(animation['static1'])
#     print(animation['movement2'])
#     print(animation['static2'])
#     sleep(.3)

frame1 = [
'                       1111111111111' + '\n'
'                      1             1' + '\n'
'                  1111   1           1' + '\n'
'                 1              1     1' + '\n'
'                 1                    1' + '\n'
'                 1                    1' + '\n'
'                 1                    1' + '\n'
'                  1111       1   1    1' + '\n'
'                      1      1   1    1' + '\n'
'                      1       111     1' + '\n'
'                      1               1' + '\n'
'                       1             1' + '\n'
'                        1    111    1' + '\n'
'                         1111   1111'
]

print(frame1[0].replace('1', random_block))




# # {
#         'static1': 
#             '\n' * 3 +
#             space + ' '*23 + random_block*13 + ' '*24 + '\n' +
#             space + ' '*22 + random_block +  ' '*13 + random_block + '\n' +
#             space + ' '*18 + random_block*4 +  ' '*3 + random_block + ' '*11 + random_block + '\n' +
#             space + ' '*17 + random_block +  ' '*14 + random_block + ' '*5 + random_block + '\n' +
#             space + ' '*17 + random_block +  ' '*20 + random_block,

#         'static2': 
#             space + ' '*22 + random_block + ' '*15 + random_block + '\n' +
#             space + ' '*23 + random_block + ' '*13 + random_block + '\n' +
#             space + ' '*24 + random_block + ' '*4 + random_block*3 + ' '*4 + random_block + '\n' +
#             space + ' '*25 + random_block*4 + ' '*3 + random_block*4, 

#         'movement1': 
#             space + ' '*17 + random_block +  ' '*20 + random_block + '\n' +
#             space + ' '*17 + random_block +  ' '*20 + random_block + '\n' +
#             space + ' '*18 + random_block*4 +  ' '*7 + random_block + ' '*3 + random_block + ' '*4 + random_block + '\n' +
#             space + ' '*22 + random_block +  ' '*6 + random_block + ' '*3 + random_block + ' '*4 + random_block + '\n' +
#             space + ' '*22 + random_block +  ' '*7 + random_block*3 + ' '*5 + random_block,
#         'movement2': 
#             space + ' '*18 + random_block*4 +  ' '*16 + random_block + '\n' +
#             space + ' '*22 + random_block +  ' '*15 + random_block + '\n' +
#             space + ' '*19 + random_block*3 +  ' '*7 + random_block + ' '*3 + random_block + ' '*4 + random_block + '\n' +
#             space + ' '*18 + random_block +  ' '*10 + random_block + ' '*3 + random_block + ' '*4 + random_block + '\n' +
#             space + ' '*19 + random_block*3 +  ' '*8 + random_block*3 + ' '*5 + random_block
#     }