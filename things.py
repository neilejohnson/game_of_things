import csv
import os
from pathlib import Path
from time import sleep
from players import display_available_players, retrieve_players
from questions import find_num_of_lines, get_random_question

#test variables
message_body = 'neil'
number = 888

#####################################
#####################################
###########     SETUP     ###########
#####################################
#####################################

#####################
##### PREP GAME #####
#####################

#define data files
data_path = str(Path(__file__).parent)+'\\Data\\'

temp_file = data_path + 'temp.txt'
answers_file = data_path + 'answers.txt'
players_file = data_path + 'players.csv'
questions_file = data_path + 'game_of_things_questions.txt'

#clear all temp game files
open(temp_file, 'w').close()
open(answers_file, 'w').close()
open(players_file, 'w+').close()

#create empty list for players and used questions
players = []
used_questions = []

#identify number of questions in the question file
num_of_questions = find_num_of_lines(questions_file)

###############################
##### GET NAME OF PLAYERS #####
###############################

#define environment as 'name'
#this communicates to the app.py what type of responses it should be taking
with open(temp_file, "a") as temp:
    temp.write("name")
with open(temp_file, "r") as temp:
    environment = temp.readline()

#displays players names as they enter game
display_available_players(players, players_file)

####################################
####################################
###########     GAME     ###########
####################################
####################################

#define environment as 'game'
#communicates to app.py to accept responses as answers
with open(temp_file, "a") as temp:
    temp.write("game")
with open(temp_file, "r") as temp:
    environment = temp.readline()

#master loop
def game_round():
    pass

#define current question
current_question = get_random_question(questions_file, num_of_questions, used_questions)

#clear answers when 

#display_question(list) from display.py
#   This will display the question and wait for answers # to reach players #
#   allow for force start within command prompt (can just type something)
#   * After 60 seconds display which players still need to answer
#   once completed, display all answers on screen and supply index number.
#   remove_answer(input: int, array):  ->  type index number to remove question. 
#   create ability to 'undo'
#   

