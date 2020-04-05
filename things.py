import csv
import os
from pathlib import Path
from time import sleep
from players import display_available_players, retrieve_players
from questions import find_num_of_lines, get_random_question

#####################################
#####################################
###########     SETUP     ###########
#####################################
#####################################

#####################
##### PREP GAME #####
#####################

# define data files
data_path = str(Path(__file__).parent)+'\\Data\\'
temp_file = data_path + 'temp.txt'
answers_file = data_path + 'answers.csv'
players_file = data_path + 'players.csv'
questions_file = data_path + 'game_of_things_questions.txt'

# clear all temp game files
open(temp_file, 'w').close()
open(answers_file, 'w').close()
open(players_file, 'w').close()

# create empty list for players and used questions
players = []
used_questions = []

# identify number of questions in the question file
num_of_questions = find_num_of_lines(questions_file)

###############################
##### GET NAME OF PLAYERS #####
###############################

#define environment as 'name'
#this communicates to the app.py what type of responses it should be taking
with open(temp_file, "w") as temp:
    temp.write("name")
with open(temp_file, "r") as temp:
    environment = temp.readline()

#displays players names as they enter game
    while environment == 'name':
        display_available_players(players, players_file)
        sleep(5)
        #'start' in app.py will change environment, breaking this while loop
        with open(temp_file, "r") as temp:
            environment = temp.readline()

####################################
####################################
###########     GAME     ###########
####################################
####################################

#master loop
while True:
    #pulls new question from question_file and drops it in used_questions list 
    current_question = get_random_question(questions_file, num_of_questions, used_questions)
    print('game is happening')
    sleep(15)




#display_question(list) from display.py
#   This will display the question and wait for answers # to reach players #
#   allow for force start within command prompt (can just type something)
#   * After 60 seconds display which players still need to answer
#   once completed, display all answers on screen and supply index number.
#   remove_answer(input: int, array):  ->  type index number to remove question. 
#   create ability to 'undo'
#   

