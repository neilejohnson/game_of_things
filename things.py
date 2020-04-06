import csv
import os
from pathlib import Path
from time import sleep
from players import display_available_players, retrieve_players
from answers import get_number_answers, retrieve_answers, format_answers, dismantle_answers, remove_answer
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

#deletes contents of txt or csv files
def clear_file(file_to_clear):
    open(file_to_clear, 'w').close()

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

    ##########################################
    ### dislay question and accept answers ###
    ##########################################

    # awaiting for answers to reach number of players
    while number_of_answers != len(players):

        #pulls new question from question_file and drops it in used_questions list
        number_of_answers = get_number_answers(answers_file)
        os.system('cls') #clear screen
        print(current_question)
        sleep(5)
        # check environment
        with open(temp_file, "r") as temp:
            environment = temp.readline()
            if environment == 'reframe':
                break
    
    os.system('cls')
    print('the answers are in!')
    sleep(5)

    #######################
    ### display answers ###
    #######################
    
    os.system('cls')

    # populate answers in answers_file
    retrieve_answers(answers, answers_file)

    round_over = 0

    while not round_over:

        gm_input = 0

        #format answers so that they have a distinct order - example [(1, {'answer': 'some answer})]
        answers = format_answers(answers)

        for answer in answers:
            print(answer[0], answer[1])
        
        gm_input = input('Which answer would you like to remove?\n')

        remove_answer(gm_input, answers, last_move)

        #for each individual answer, check if gm_input is equal to string answer[0]
        if gm_input in [str(answer[0]) for answer in answers]:
            last_move = remove_answer(gm_input, answers, last_move)
        elif gm_input == 'undo':
            #put last move back into answers
            answers.append(last_move)
        else:
            print('not a valid response')

#!!! gives not a valid response unless undo is used. undo doesn't actually work.
#!!! once answers reach 1 then it goes to 'the answers are in!'

        #if there is only one answer left, the round is over and it breaks this loop
        if len(answers) == 1:
            clear_file(answers_file)
            round_over = 'yes'

            #dismantle list for renumbering in next loop
        answers = dismantle_answers(answers)

    answers = dismantle_answers(answers)

    #while len(answers) != 1:
#     display answers using function
#     gm_input = input('')
#     display answers using function  

###1. gets random question
###2. clear answers file
###3. DISPLAY - RANDOM QUESTION
###4. collect answers
#5. *** after 45 seconds, if someone hasn't yet submitted an answer, call them out.
#6. *** text force to carry to the next stage
###7. display answers on screen
###8. allow for number to be input to delete them
###9. If answer == 1 then the round is over.
#10. short animation plays. 


#display_question(list) from display.py
#   This will display the question and wait for answers # to reach players #
#   allow for force start within command prompt (can just type something)
#   * After 60 seconds display which players still need to answer
#   once completed, display all answers on screen and supply index number.
#   remove_answer(input: int, array):  ->  type index number to remove question. 
#   create ability to 'undo'
#   

