import os
from time import sleep
from random import randint
from colored import fg, attr
from players import retrieve_players

colors = [87, 158, 216, 187, 225, 169, 141, 147]
blocks = ['░','▒','▓']

def display_animation(winner, blocks, colors):
    #define variables and random instances
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

    #character animation
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

#display list of players as they come in
def display_available_players(players: list, players_file: str, random_block: str):
    retrieve_players(players, players_file)
    os.system('cls')
    print(random_block * 210 + '\n\n')

    if players: #players contains any value
        for player in players:
            if player: #remove any empty lines
                print('\t\t'+player['name'])
        print(('\n' * (13 - len(players)) + random_block*140))
    else:
        print('\t\t'+'No players have joined the game yet.')
        print('\n' * 12 + random_block * 140)

def display_current_question(current_question: str, random_block: str, random_color: str):
    print(random_color + '\n' + random_block * 70)
    print(random_block * 10 + ' ' * 50 + random_block * 10)
    print(random_block * 5 + ' ' * 60 + random_block * 5)
    print(random_block * 2 + ' ' * 66 + random_block * 2 + '\n')
    print(attr('reset') + '     ' + current_question.upper() + '\n' * 6)
    print(random_color + '\t\t\tplease submit your answers now\n\n')
    print(random_block * 2 + ' ' * 66 + random_block * 2)
    print(random_block * 5 + ' ' * 60 + random_block * 5)
    print(random_block * 10 + ' ' * 50 + random_block * 10)
    print(random_block * 70 + attr('reset'))

def display_homescreen(blocks, colors):
    random_color = fg(colors[randint(0,len(colors)-1)])
    random_block = blocks[randint(0,len(blocks)-1)]
    
    os.system('cls')
    #set random color
    print(random_color)

    print('\n')
    print(random_block * 70 + '\n')
    print(random_block * 70 + '\n')
    print(random_block * 70 + '\n')

    print('\t\tTHE\n\t\t\tGAME\n\t\t\t\t OF\n\t\t\t\t\tTHINGS\n')

    print(random_block * 70 + '\n')
    print(random_block * 70 + '\n')
    print(random_block * 70)

    #clear random color
    print(attr('reset'))

def display_answers_header(current_question, random_block, random_color):
    print(random_color + '\n' * 2 + random_block * 70)
    print(' ' + current_question.upper())
    print(random_color + random_block * 70+'\n'*2 + attr('reset'))

def display_round(round_number):
    os.system('cls')
    print('\n'*8)
    print('\t\t\t      ROUND {}'.format(round_number))
    print('\n'*10)
    sleep(3.5)
    os.system('cls')
    sleep(2)

def display_answers_in():
    os.system('cls')
    print('\n'*8)
    print('\t\t\tThe answers are in!')
    print('\n'*10)
    sleep(3.5)
    os.system('cls')
    sleep(2)