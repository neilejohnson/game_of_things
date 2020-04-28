import csv
import os
from random import randint
from time import sleep

from colored import fg, attr
from pathlib import Path

from Resources.answers import get_number_answers, retrieve_answers, format_answers, dismantle_answers, remove_answer
from Resources.display import display_answers_in, display_animation, display_homescreen, display_available_players, display_current_question, display_answers_header, display_round
from Resources.misc import clear_file
from Resources.players import retrieve_players, retreive_winning_player
from Resources.questions import find_num_of_lines, get_random_question

#####################################
#####################################
###########     SETUP     ###########
#####################################
#####################################

# Display Settings: 
# Size: 125% 
# Resolution: 1920x1080

# Windows PowerShell Settings:
# Font Size: 36
# Font: Lucida Console
# Screen Background: Black
# Screen maximized

#####################
##### PREP GAME #####
#####################

# define data files
data_path = str(Path(__file__).parent)+'\\Data\\'
temp_file = data_path + 'temp.txt'
answers_file = data_path + 'answers.csv'
players_file = data_path + 'players.csv'
questions_file = data_path + 'game_of_things_questions.txt'

# define colored module variables
colors = [87, 158, 216, 187, 225, 169, 141, 147]
blocks = ['░','▒','▓']
reset = attr('reset')

# clear all temp game files
clear_file(temp_file)
clear_file(answers_file)
clear_file(players_file)

# create empty list for players and used questions
players = []
answers = []
used_questions = []
number_of_answers = 0
last_move = 0
round_number = 1

# identify number of questions in the question file
# this allows for questions to be added or removed from quesions_file 
num_of_questions = find_num_of_lines(questions_file)

#displays the Game of Things homescreen
display_homescreen(blocks, colors)

###############################
##### GET NAME OF PLAYERS #####
###############################

#define environment as 'name'
#this communicates to the app.py what type of responses it should be taking
with open(temp_file, "w") as temp:
    temp.write("name")
with open(temp_file, "r") as temp:
    environment = temp.readline()

#set random elements
random_color = fg(colors[randint(0,len(colors)-1)])
random_block = blocks[randint(0,len(blocks)-1)]

#displays players names as they enter game
print(random_color)
while environment == 'name':
    display_available_players(players, players_file, random_block)

    #'start' in app.py will change environment, breaking this while loop
    with open(temp_file, "r") as temp:
        environment = temp.readline()
print(reset)

####################################
####################################
###########     GAME     ###########
####################################
####################################

#begin master loop for each round
while True:

    # make sure environment is set to game in case last round was forced through
    with open(temp_file, "w") as temp:
        temp.write("game")

    ##################
    ### prep round ###
    ##################

    # grabs a new question to start the round.
    current_question = get_random_question(questions_file, num_of_questions, used_questions)

    #clears answer file for new round
    clear_file(answers_file)

    number_of_answers = 0

    #displays which round number they are on
    display_round(round_number)

    ##########################################
    ### dislay question and accept answers ###
    ##########################################

    #set random elements
    random_color = fg(colors[randint(0,len(colors)-1)])
    random_block = blocks[randint(0,len(blocks)-1)]

    # awaiting for answers to reach number of players
    while number_of_answers != len(players):

        #pulls new question from question_file and drops it in used_questions list
        number_of_answers = get_number_answers(answers_file)

        os.system('cls')

        #display_current_question
        display_current_question(current_question, random_block, random_color)

        # check environment. If 'force' message received, moves forward without all answers
        with open(temp_file, "r") as temp:
            environment = temp.readline()
            if environment == 'reframe':
                break
    print(reset)

    #answers are in screen
    display_answers_in()

    #######################
    ### display answers ###
    #######################
    
    os.system('cls')

    # populate answers list from answers_file
    retrieve_answers(answers, answers_file)

    round_over = False

    random_color = fg(colors[randint(0,len(colors)-1)])
    random_block = blocks[randint(0,len(blocks)-1)]

    while not round_over:

        #clear gm_input
        gm_input = 0

        #format answers so that they have a distinct order - example [(1, {'answer': 'some answer})]
        answers = format_answers(answers)
        
        display_answers_header(current_question, random_block, random_color)

        for answer in answers:
            print('   ' + str(answer[0]) + '  ' + answer[1])

        print(random_color + '\n' * (11 - len(answers)) + random_block * 70 + reset)

        gm_input = input('\nWhich answer would you like to remove?\n')
        
        #for each individual answer, check if gm_input is equal to string answer[0]
        if gm_input in [str(answer[0]) for answer in answers]:
            last_move = remove_answer(gm_input, answers, last_move)
        elif gm_input.lower() == 'undo':

            #put last move back into answers
            answers.append(last_move)

        #if there is only one answer left, the round is over and it breaks this loop
        if len(answers) == 1:

            winner_round = retreive_winning_player(answers, answers_file, players_file)
            
            display_animation(winner_round, blocks, colors)

            os.system('cls')
            sleep(2)
            round_number += 1

            #clear answer file for next round
            clear_file(answers_file)

            round_over = True

        #dismantle list for renumbering in next loop
        answers = dismantle_answers(answers)