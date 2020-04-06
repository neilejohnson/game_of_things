import os
import csv
from pprint import pprint
from time import sleep

#test variables
# answers = [
#     {
#     'answer': 'this is the answer', 
#     'number': '+508-444-2645'
#     }, 
#     {
#     'answer': 'this is the second answer', 
#     'number': '+508-444-2555'
#     },
#     {
#     'answer': 'this is the third answer', 
#     'number': '+555-444-2505'
#     }
# ]

# last_move = ''

#passes incoming number 
#!!!!! this probably doesn't work
def check_number_answer(incoming_number: str, answers_file: str) -> str:
    with open(answers_file, 'r') as csv_file:
        for line in csv.DictReader(csv_file, fieldnames=('name', 'number')):
            if incoming_number == line['number']:
                return ''
            return incoming_number

# adds new player to answers.csv
def add_answer(message_body: str, number: str, answers_file: str):
    with open(answers_file, "a", newline="") as doc:
        writer = csv.writer(doc)
        writer.writerow([message_body, number])

#pass in gm_input and pop cooresponding answer as return value
def remove_answer(gm_input: str, answers: list, last_move: str) -> tuple:
    for answer in answers:
        if str(answer[0]) == gm_input:
            #must be -1 as the player's answer display index starts at 1 not 0
            return answers.pop(int(gm_input)-1)

def get_number_answers(answers_file: str) -> int:
    answers=[]
    with open(answers_file, 'r') as csv_file:
        for line in csv_file:
            answers.append(line)
    return len(answers)

#refreshes answers list to capture all answers currently in answers_file
def retrieve_answers(answers: list, answers_file: str):
    #clear answers
    del answers[:]
    #append ordered dicts to answers list
    with open(answers_file, 'r') as csv_file:
        for line in csv.DictReader(csv_file, fieldnames=('answer', 'number')):
            answers.append(dict(line)['answer'])

################################
### structuring answers list ###
################################

# returns constructed list of answers to display in console 
# example [(1, 'some answer'), (2, 'another answer')]
def format_answers(answers: list) -> list:
    answer_number = 1
    formatted_answers = []
    for answer in answers:
        #take each item and return them as a tuple
        formatted_answers.append(tuple([answer_number, answer]))
        answer_number += 1
    return formatted_answers

#returns deconstructed list of current answers for renumbering in display
# example ['some answer', 'another answer']
def dismantle_answers(answers: list) -> list:
    output = []
    for answer in answers:
        if answer:
            output.append(answer[1])
    return output

#should not be infinite loop
# while True:
#     #os.system('cls')
#     #build list
    

#     while len(answers) != 1:
        
#         display_answers(answers)
#         gm_input = input('***')
#         sleep(5)
#         dismantle_answers
#         #display answers using function   


# #displays list of 

# format_answers(answers)
# def display_answers(answers):
#     dismantle_answers(answers)
    

    


    #  for answer in answers:
    #     print(answer[0], answer[1]['answer'])
    # gm_input = input('')



####################################################


# from questions import find_num_of_lines, get_random_question

# used_questions = []

# questions_file = 'game_of_things_questions.txt'

# num_of_questions = find_num_of_lines(questions_file)
# print(get_random_question(questions_file, num_of_questions, used_questions))

# print(used_questions)