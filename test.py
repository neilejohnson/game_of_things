# import csv
# from answers import get_number_answers
# from pathlib import Path
from display import display_current_question
from time import sleep
from colored import fg, attr
import os
from random import randint
random_block = '░'

colors = [87, 158, 216, 187, 225, 169, 141, 147]

random_color = fg(colors[randint(0,len(colors)-1)])

os.system('cls')
display_current_question('how are you?', random_block, random_color)