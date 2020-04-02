import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def top():
    print('*******************************************************************************')

def sides3():
    print('***                                                                         ***')

def sides2():
    print('**                                                                           **')

def sides1():
    print('*                                                                             *')

def question_display(question):
    os.system('cls')
    top()
    sides3()
    sides2()
    sides1()
    print('')
    print(bcolors.UNDERLINE+'\t'+question.upper() + bcolors.ENDC)
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('\t\t\t\tplease send your response now')
    print('')
    sides1()
    sides2()
    sides3()
    top()

question_display('If you were a ghost, who would you haunt?')


def display_question(current_question):
    pass #displays current question - using design until all questions are in