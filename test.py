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

data_path = str(Path(__file__).parent)+'\\Data\\'
temp_file = data_path + 'temp.txt'
answers_file = data_path + 'answers.csv'
players_file = data_path + 'players.csv'
questions_file = data_path + 'game_of_things_questions.txt'

display_answers_in()