# import csv
# from answers import get_number_answers
# from pathlib import Path
from display import display_current_question, display_round, display_animation
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

colors = [87, 158, 216, 187, 225, 169, 141, 147]
blocks = ['░','▒','▓']

display_animation('Jordan', blocks, colors)
