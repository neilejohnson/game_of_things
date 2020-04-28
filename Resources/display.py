import os
from time import sleep
from random import randint
from colored import fg, attr
from Resources.players import retrieve_players

colors = [87, 158, 216, 187, 225, 169, 141, 147]
blocks = ['░','▒','▓']

def _winning_message(winner: str) -> str:
    messages = [
        ' Congrats, {}!! Great job. ', 
        '{}, you are a smart cookie.',
        ' I never doubted you, {}!! ',
        'Can you believe it? {} won.', 
        '       {} is my hero       ', 
        ' Smooth, {}.  Real smooth. ', 
        '    {} hath triumphed!!    ', 
        '  Three Cheers for {}!!!!  ', 
        ' Ahhhhh! Wow. Good job {}. ', 
        ' I am so proud of you, {}! ', 
        '  So stoked for you, {}!!  ', 
        ' And the round goes to {}! ', 
        ' {}, did you hear? You won ', 
        'Boy howdy, {}. You did good', 
        'Not surprised! {} is smart.', 
        ' {} is my favorite human!! ', 
        '   {} is just that good.   ', 
        'Look at {}, cleaning house!', 
        '      Miraculous, {}!      ', 
        '      Stupendous, {}!      ', 
        '     Dynamite job, {}!     ', 
        '  A colossal win for {}!!  ', 
        ' {}, consider me impressed ', 
        ' {}, what a grand display! ', 
        ' Woop! Woop! Go get em {}! ', 
        'Wowie Zowie! {} is a beast.', 
        '    {}! I’m not worthy!    ', 
        'Gosh darn it. {} is so cool', 
        '    Nice, {}. Real nice    ', 
        '  {} is one gnarly human.  ', 
        'Capital job, {}! As always.', 
        '  Hear the news? {} won!!  ', 
        '      {} is superior.      ', 
        '       {}, nice job.       ', 
        '   Flawless victory, {}!!  ', 
        'Yes, {}! You are so mighty.', 
        '     {} is an expert!!     ', 
        '   {} has a decent brain   '
    ]

    random_message = messages[randint(0,len(messages)-1)]

    return random_message.format(winner)

def display_animation(winner, blocks, colors):
    #define variables and random instances
    reset = attr('reset')
    space = '   '
    random_color = fg(colors[randint(0,len(colors)-1)])
    random_block = blocks[randint(0,len(blocks)-1)]

    animations = [
        #1 computer
        {
            'frame1':
                '\n' + 
                '\n' + 
                '\n' + 
                '\n' + 
                '                 1111111111111111111111111' + '\n' +
                '                1                         1' + '\n' +
                '      11 11    1   111111111111111111111   1    11 11' + '\n' +
                '     1111111   1   1                   1   1   1111111' + '\n' +
                '     1111111   1   1   1          1    1   1   1111111' + '\n' +
                '      11111    1   1                   1   1    11111' + '\n' +
                '       111     1   1                   1   1     111' + '\n' +
                '        1      1   1     1      1      1   1      1' + '\n' +
                '               1   1      111111       1   1' + '\n' +
                '               1   1                   1   1' + '\n' +
                '               1   111111111111111111111   1' + '\n' +
                '                1                         1' + '\n' +
                '                 1111111111111111111111111' + '\n',
            'frame2':
                '\n' + 
                '\n' + 
                '\n' + 
                '\n' + 
                '                 1111111111111111111111111' + '\n' +
                '                1                         1' + '\n' +
                '     11 11     1   111111111111111111111   1     11 11' + '\n' +
                '    1111111    1   1                   1   1    1111111' + '\n' +
                '    1111111    1   1   1          1    1   1    1111111' + '\n' +
                '     11111     1   1                   1   1     11111' + '\n' +
                '      111      1   1                   1   1      111' + '\n' +
                '       1       1   1     1      1      1   1       1' + '\n' +
                '               1   1      111111       1   1' + '\n' +
                '               1   1                   1   1' + '\n' +
                '               1   111111111111111111111   1' + '\n' +
                '                1                         1' + '\n' +
                '                 1111111111111111111111111' + '\n'
        },
        #2 bird
        {
            'frame1':
                '\n' + 
                '\n' + 
                '\n' + 
                '\n' + 
                '                     11111111111111' + '\n' +
                '                    1              1' + '\n' +
                '                   1                1' + '\n' +
                '                 11   1              11' + '\n' +
                '               11                1     11' + '\n' +
                '            111                          111' + '\n' +
                '          11                                11' + '\n' +
                '         1        1      1111        1        1' + '\n' +
                '        1      111 1                1 111      1' + '\n' +
                '         111111     1              1     111111' + '\n' +
                '                     11111111111111' + '\n' +
                '                        1      1' + '\n' +
                '                       1        1' + '\n',
            'frame2':
                '\n' + 
                '\n' + 
                '\n' + 
                '\n' + 
                '         111         11111111111111         111' + '\n' +
                '        1   1       1              1       1   1' + '\n' +
                '        1   111   1                1   111    1' + '\n' +
                '        1       111   1              111       1' + '\n' +
                '         1                       1            1' + '\n' +
                '          1                                  1' + '\n' +
                '           111                            111' + '\n' +
                '              11111      1111        11111' + '\n' +
                '                   1                1' + '\n' +
                '                    1              1' + '\n' +
                '                     11111111111111' + '\n' +
                '                        1      1' + '\n' +
                '                       1        1' + '\n'
        },
        #3 slime
        {
            'frame1':
                '\n' + 
                '\n' + 
                '\n' + 
                '\n' + 
                '\n' + 
                '                     11111111111111111111' + '\n' +
                '                  111                    1' + '\n' +
                '                11                        11' + '\n' +
                '               1                            1' + '\n' +
                '              1                              1' + '\n' +
                '             1       1                        1' + '\n' +
                '            1                            1     1' + '\n' +
                '           1                                   1' + '\n' +
                '           1             11111111111111         1' + '\n' +
                '           1                                    1' + '\n' +
                '            111111111111111111111111111111111111' + '\n' +
                '\n',
            'frame2':
                '\n' + 
                '\n' + 
                '\n' + 
                '                    1111111111111111111111' + '\n' +
                '                 111                      111' + '\n' +
                '               11                            11' + '\n' +
                '              1                                1' + '\n' +
                '             1                                  1' + '\n' +
                '            1       1                            1' + '\n' +
                '           1                            1        1' + '\n' +
                '           1                                     1' + '\n' +
                '            1                                   1' + '\n' +
                '            1           11111111111111          1' + '\n' +
                '             11                               11' + '\n' +
                '               1                             1' + '\n' +
                '                11111111111111111111111111111' + '\n' +
                '\n'
        },
        #4 ghosts
        {
            'frame1':
                '\n' + 
                '\n' + 
                '\n' + 
                '\n' + 
                '              111111111              111111111' + '\n' +
                '             1         1            1         1' + '\n' +
                '            1   1    1  1          1  1    1   1' + '\n' +
                '            1           1          1           1' + '\n' +
                '            1     11    1          1    11     1' + '\n' +
                '            1           1          1           1' + '\n' +
                '            1           1          1           1' + '\n' +
                '             1  11  11  1          1  11  11  1' + '\n' +
                '              11  11  11            11  11  11' + '\n' +
                '\n' + 
                '\n' + 
                '\n' + 
                '\n',
            'frame2':
                '\n' + 
                '\n' + 
                '\n' + 
                '\n' + 
                '              111111111              111111111' + '\n' +
                '             1         1            1         1' + '\n' +
                '            1   1    1  1          1  1    1   1' + '\n' +
                '            1           1          1           1' + '\n' +
                '            1     11    1          1    11     1' + '\n' +
                '            1           1          1           1' + '\n' +
                '            1           1          1           1' + '\n' +
                '            1  11  11  1            1  11  11  1' + '\n' +
                '             11  11  11              11  11  11' + '\n' +
                '\n' + 
                '\n' + 
                '\n' + 
                '\n'
        },
        #5 alien
        {
            'frame1':
                '\n' + 
                '\n' + 
                '             11111111                 11111111' + '\n' +
                '            11 1    11               11  1   11' + '\n' +
                '            11      11               11      11' + '\n' +
                '            11      11               11      11' + '\n' +
                '            11      11               11      11' + '\n' +
                '             11111111   11111111111   11111111' + '\n' +
                '                11111111111111111111111111' + '\n' +
                '             1111111111111111111111111111111' + '\n' +
                '               11       11     111111111111111' + '\n' +
                '                                11111111111111' + '\n' +
                '                              111111111111111' + '\n' +
                '                 1111111111111111111111111' + '\n' +
                '                    1111111111111111111111' + '\n' +
                '                     111         1111' + '\n' +
                '                   11111       111111' + '\n',
            'frame2':
                '\n' + 
                '\n' + 
                '             11111111                 11111111' + '\n' +
                '            11 1    11               11  1   11' + '\n' +
                '            11      11               11      11' + '\n' +
                '            11      11               11      11' + '\n' +
                '            11      11               11      11' + '\n' +
                '             11111111   11111111111   11111111' + '\n' +
                '                11111111111111111111111111' + '\n' +
                '             1111111111111111111111111111111' + '\n' +
                '             111111111111111111111111111111111' + '\n' +
                '             111111111111111111111111111111111' + '\n' +
                '              1111111111111111111111111111111' + '\n' +
                '                 1111111111111111111111111' + '\n' +
                '                    1111111111111111111111' + '\n' +
                '                     111         1111' + '\n' +
                '                   11111       111111' + '\n'
        },
        #6 robot
        {
            'frame1':
                '\n' + 
                '\n' + 
                '\n' + 
                '\n' + 
                '                1111111111111111111111111' + '\n' +
                '               111111111111111111111111111' + '\n' +
                '             1111   1                1  1111' + '\n' +
                '             1111                       1111' + '\n' +
                '             1111111111111111111111111111111' + '\n' +
                '                     1111     11111' + '\n' +
                '                      111111111111' + '\n' +
                '                     1 1111111111 1' + '\n' +
                '                    1  1111111111  1' + '\n' +
                '                   1    11111111    1' + '\n' +
                '                        11111111' + '\n' +
                '                         1    1' + '\n' +
                '                         1    1' + '\n',
            'frame2':
                '\n' + 
                '\n' + 
                '\n' + 
                '\n' + 
                '                1111111111111111111111111' + '\n' +
                '               111111111111111111111111111' + '\n' +
                '             1111   1                1  1111' + '\n' +
                '             1111                       1111' + '\n' +
                '             1111111111111111111111111111111' + '\n' +
                '                     1111     11111' + '\n' +
                '                 111  111111111111  111' + '\n' +
                '                    11 1111111111 11' + '\n' +
                '                       1111111111' + '\n' +
                '                        11111111' + '\n' +
                '                        11111111' + '\n' +
                '                         1    1' + '\n' +
                '                         1    1' + '\n'
        },
        #7 owl
        {
            'frame1':
                '\n' + 
                '\n' + 
                '\n' + 
                '                      11                11' + '\n' +
                '                    11  1111111111111111  1' + '\n' +
                '                   1                       1' + '\n' +
                '                  1                        1' + '\n' +
                '                  1   1                1   1' + '\n' +
                '                  1       1111111111       1' + '\n' +
                '                  1     111111111111111    1' + '\n' +
                '                  1                        1' + '\n' +
                '                 11      1111111111111     11' + '\n' +
                '                1                            1' + '\n' +
                '                 11                        11' + '\n' +
                '                   1                      1' + '\n' +
                '                    1111111111111111111111' + '\n' +
                '                        1111       1111' + '\n',
            'frame2':
                '\n' + 
                '\n' + 
                '\n' + 
                '                      11                11' + '\n' +
                '                    11  1111111111111111  1' + '\n' +
                '                   1                       1' + '\n' +
                '                  1                        1' + '\n' +
                '                  1   1                1   1' + '\n' +
                '                  1       1111111111       1' + '\n' +
                '                  1     111111111111111    1' + '\n' +
                '                 11      1111111111111     11' + '\n' +
                '                1                            1' + '\n' +
                '                 11                        11' + '\n' +
                '                   1                      1  ' + '\n' +
                '                   1                      1' + '\n' +
                '                    1111111111111111111111' + '\n' +
                '                        1111       1111' + '\n'
        },
        #8 creature
        {
            'frame1':
                '\n' + 
                '\n' + 
                '\n' + 
                '                       1111111111111' + '\n' +
                '                      1             1' + '\n' +
                '                  1111   1           1' + '\n' +
                '                 1              1     1' + '\n' +
                '                 1                    1' + '\n' +
                '                 1                    1' + '\n' +
                '                 1                    1' + '\n' +
                '                  1111       1   1    1' + '\n' +
                '                      1      1   1    1' + '\n' +
                '                      1       111     1' + '\n' +
                '                      1               1' + '\n' +
                '                       1             1' + '\n' +
                '                        1    111    1' + '\n' +
                '                         1111   1111' + '\n',
            'frame2':
                '\n' + 
                '\n' + 
                '\n' + 
                '                       1111111111111' + '\n' +
                '                      1             1' + '\n' +
                '                  1111   1           1' + '\n' +
                '                 1              1     1' + '\n' +
                '                 1                    1' + '\n' +
                '                  1111                1' + '\n' +
                '                      1               1' + '\n' +
                '                   111       1   1    1' + '\n' +
                '                  1          1   1    1' + '\n' +
                '                   111        111     1' + '\n' +
                '                      1               1' + '\n' +
                '                       1             1' + '\n' +
                '                        1    111    1' + '\n' +
                '                         1111   1111' + '\n'
        }
    ]

    random_animation = animations[randint(0,len(animations)-1)]
    random_message = _winning_message(winner)

    #character animation
    print(random_color)
    for x in range(14):
        os.system('cls')
        if x%2==0:
            print(random_animation['frame1'].replace('1', random_block))
        else:
            print(random_animation['frame2'].replace('1', random_block))
        print('\n\t      ' + space + random_message + '\n')
        sleep(.3)
    print(reset)

#display list of players as they come in
def display_available_players(players: list, players_file: str, random_block: str):
    retrieve_players(players, players_file)
    os.system('cls')
    print(random_block * 70)
    print(random_block * 7 + '            Submit your name to join the game           ' + random_block * 7) 
    print(random_block * 70 + '\n\n')

    if players: #players contains any value
        for player in players:
            if player: #remove any empty lines
                print('\t\t'+player['name'])
        print(('\n' * (13 - len(players)) + random_block*140))
    else:
        print('\t\t'+'No players have joined the game yet.')
        print('\n' * 12 + random_block * 140)

    # hold for 5 seconds before refreshing
    sleep(5)

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

    # hold on current question before it resets
    sleep(5)

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

    # clear random color
    print(attr('reset'))

    # hold on homescreen
    sleep(7)

    # short blank screen
    os.system('cls')
    sleep(1)

def display_answers_header(current_question, random_block, random_color):
    print(random_color + '\n' * 2 + random_block * 70)
    print(' ' + current_question.upper())
    print(random_color + random_block * 70+'\n'*2 + attr('reset'))

def display_round(round_number):
    os.system('cls')
    print('\n'*8)
    print('\t\t\t      ROUND {}'.format(round_number))
    print('\n'*10)

    # hold on round
    sleep(3.5)
    
    os.system('cls')
    
    #hold on blank screen
    sleep(2)

def display_answers_in():
    os.system('cls')
    print('\n'*8)
    print('\t\t\tThe answers are in!')
    print('\n'*10)

    # hold on answers in
    sleep(3.5)
    os.system('cls')

    # hold on blank screen
    sleep(2)