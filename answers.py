import os
from pprint import pprint

#test variables
answers = [
    {
    'answer': 'this is the answer', 
    'number': '+508-444-2645'
    }, 
    {
    'answer': 'this is the second answer', 
    'number': '+508-444-2555'
    },
    {
    'answer': 'this is the third answer', 
    'number': '+555-444-2505'
    }
]

last_move = ''

#pass in gm_input and pop cooresponding answer as return value
def remove_answer(gm_input: str, answers: list, last_move: str) -> tuple:
    for answer in answers:
        if str(answer[0]) == gm_input:
            #must be -1 as the player's answer display index starts at 1 not 0
            return answers.pop(int(gm_input)-1)

################################
### structuring answers list ###
################################

#returns constructed list of answers to display in console 
def format_answers(answers: list) -> list:
    answer_number = 1
    formatted_answers = []
    for answer in answers:
        #take each item and return them as a tuple
        formatted_answers.append(tuple([answer_number, answer]))
        answer_number += 1
    return formatted_answers

#returns deconstructed list of current answers for renumbering in display
def dismantle_answers(answers: list) -> list:
    output = []
    for answer in answers:
        if answer:
            output.append(answer[1])
    return output

#should not be infinite loop
while True:
    #os.system('cls')
    #build list
    answers = format_answers(answers)
    for answer in answers:
        print(answer[0], answer[1]['answer'])
    gm_input = input('')

    #for each individual answer, check if gm_input is equal to string answer[0]
    if gm_input in [str(answer[0]) for answer in answers]:
        last_move = remove_answer(gm_input, answers, last_move)
    elif gm_input == 'undo':
        #put last move back into answers
        answers.append(last_move)
    else:
        print('not a valid response')

    #dismantle list for renumbering in next loop
    answers = dismantle_answers(answers)


####################################################


# from questions import find_num_of_lines, get_random_question

# used_questions = []

# questions_file = 'game_of_things_questions.txt'

# num_of_questions = find_num_of_lines(questions_file)
# print(get_random_question(questions_file, num_of_questions, used_questions))

# print(used_questions)