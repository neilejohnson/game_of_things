import os
from time import sleep
from random import randint
from colored import fg, attr

def display_animation(winner):
    #define variables and random instances
    colors = [87, 158, 216, 187, 225, 169, 141, 147]
    blocks = ['░','▒','▓']
    reset = attr('reset')
    space = '   '
    random_color = fg(colors[randint(0,len(colors)-1)])
    random_block = blocks[randint(0,len(blocks)-1)]

    animations = [
    {
        'static1': 
            '\n' * 3 +
            space + ' '*23 + random_block*13 + ' '*24 + '\n' +
            space + ' '*22 + random_block +  ' '*13 + random_block + '\n' +
            space + ' '*18 + random_block*4 +  ' '*3 + random_block + ' '*11 + random_block + '\n' +
            space + ' '*17 + random_block +  ' '*14 + random_block + ' '*5 + random_block + '\n' +
            space + ' '*17 + random_block +  ' '*20 + random_block,

        'static2': 
            space + ' '*22 + random_block + ' '*15 + random_block + '\n' +
            space + ' '*23 + random_block + ' '*13 + random_block + '\n' +
            space + ' '*24 + random_block + ' '*4 + random_block*3 + ' '*4 + random_block + '\n' +
            space + ' '*25 + random_block*4 + ' '*3 + random_block*4, 

        'movement1': 
            space + ' '*17 + random_block +  ' '*20 + random_block + '\n' +
            space + ' '*17 + random_block +  ' '*20 + random_block + '\n' +
            space + ' '*18 + random_block*4 +  ' '*7 + random_block + ' '*3 + random_block + ' '*4 + random_block + '\n' +
            space + ' '*22 + random_block +  ' '*6 + random_block + ' '*3 + random_block + ' '*4 + random_block + '\n' +
            space + ' '*22 + random_block +  ' '*7 + random_block*3 + ' '*5 + random_block,
        'movement2': 
            space + ' '*18 + random_block*4 +  ' '*16 + random_block + '\n' +
            space + ' '*22 + random_block +  ' '*15 + random_block + '\n' +
            space + ' '*19 + random_block*3 +  ' '*7 + random_block + ' '*3 + random_block + ' '*4 + random_block + '\n' +
            space + ' '*18 + random_block +  ' '*10 + random_block + ' '*3 + random_block + ' '*4 + random_block + '\n' +
            space + ' '*19 + random_block*3 +  ' '*8 + random_block*3 + ' '*5 + random_block
    }
    # ,
    # #second animation
    # {
    # 'static1': '', 'static2': '', 'movement1': '', 'movement2': ''}
    ]

    random_animation = animations[randint(0,len(animations)-1)]

    for x in range(14):
        os.system('cls')
        print(random_color + random_animation['static1'])
        if x%2==0:
            print(random_animation['movement1'])
        else:
            print(random_animation['movement2'])
        print(random_animation['static2'])
        print('\n'*2 + '\t'*2 + space + 'Congrats, {}! Great job.'.format(winner) + '\n'*1 + reset)
        sleep(.4)

def display_question(current_question):
        #define variables and random instances
    # colors = [87, 158, 216, 187, 225, 169, 141, 147]
    # reset = attr('reset')
    # random_color = fg(colors[randint(0,len(colors)-1)])

    # print('*'*70+'\n')
    # print('')
    pass
    