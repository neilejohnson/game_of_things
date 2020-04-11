import os
from random import randint
from colored import fg, attr

def print_animation(winner):
    #define variables and random instances
    colors = [87, 158, 216, 187, 225, 169, 141, 147]
    blocks = ['░','▒','▓']
    reset = attr('reset')
    random_color = fg(colors[randint(0,len(colors)-1)])
    random_block = blocks[randint(0,len(blocks)-1)]

    animations = [
    #first animation
    {'static1': 
        '\n'*3 +
        ' '*23 + random_block*13 + ' '*24 + '\n' +
        ' '*22 + random_block +  ' '*13 + random_block + '\n' +
        ' '*18 + random_block*4 +  ' '*3 + random_block + ' '*11 + random_block + '\n' +
        ' '*17 + random_block +  ' '*14 + random_block + ' '*5 + random_block + '\n' +
        ' '*17 + random_block +  ' '*20 + random_block + '\n',

    'static2': 
        ' '*22 + random_block + ' '*15 + random_block + '\n' +
        ' '*23 + random_block + ' '*13 + random_block + '\n' +
        ' '*24 + random_block + ' '*4 + random_block*3 + ' '*4 + random_block + '\n' +
        ' '*25 + random_block*4 + ' '*3 + random_block*4 + '\n', 
        'movement1': '', 'movement2': ''},
    #second animation
    {'static1': '', 'static2': '', 'movement1': '', 'movement2': ''},
    ]
    

    random_animation = animations[randint(0,len(animations)-1)]

    for x in range(3):
        os.system('cls')
        print(random_animation['static1'])
        print(random_animation['static2'])
        print(random_color+('\n'*3))
        print(' '*23+ random_block*13 + ' '*24 + reset)
        print(' '*24+ random_block*13 + ' '*23)
        
        print(x, animations)

winner = 'Jordan'
print_animation(winner)




#print static 1
#print animation 1
#print static 2 (with message)
#clear
#print static 1
#print animation 2
#print static 2 (with message)
#clear



#first animation
# 17   1*     20    1*    21
# 17   1*     20    1*    21
# 18     4*   7   1*   3    1*      4      1*    21
# 22    1*    6    1*    3    1*    4    1*   21  
# 22    1*    7    3*        5    1*   21  

#second animation

# 18     4*    16    1*     21
# 22   1*    15    1*     21
# 19   3*     7    1*   3    1*    4        1*     21
# 18      1*    10      1*     3    1*     4    1*    21
# 19   3*    8   3*   6  1*   21

# 22    1*   15   1*   21  
# 23    1*    13     1*   22
# 24    1*     4     3*   4   1*      23
# 25    4*    3   4*    24
# \n
# \n
# \n
# \n
# \n


# color_list = [bcolors.OKBLUE, bcolors.OKGREEN]

# def top(random_color):
#     print(random_color+'*'*70 + bcolors.ENDC)

# top(color_list[0])

#    print(bcolors.random_color+'*'*70 + bcolors.ENDC)

# def sides3():
#     print('***'*3                                                                         '***'*3)

# def sides2():
#     print('**                                                                           **')

# def sides1():
#     print('*                                                                             *')

# def question_display(question):
#     os.system('cls')
#     top()
#     sides3()
#     sides2()
#     sides1()
#     print('')
#     print(bcolors.UNDERLINE+'\t'+question.upper() + bcolors.ENDC)
#     print('')
#     print('')
#     print('')
#     print('')
#     print('')
#     print('')
#     print('\t\t\t\tplease send your response now')
#     print('')
#     sides1()
#     sides2()
#     sides3()
#     top()

# question_display('If you were a ghost, who would you haunt?')

# def display_question(current_question):
#     pass #displays current question - using design until all questions are in