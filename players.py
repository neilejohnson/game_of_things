import csv
import os
from threading import Timer

################################
## ADDS PLAYER TO PLAYERS.CSV ##
################################

#tested and works. do not need to pass argument
def add_player(message_body: str, number: str, players_file: str):
    with open(players_file, "a", newline="") as doc:
        writer = csv.writer(doc)
        writer.writerow([message_body, number, 0])

########################################
## PLAYERS.CSV APPEND TO PLAYERS LIST ##
########################################

#refreshes players list to capture all players currently in players_file
def retrieve_players(players: list, players_file: str):
    #clear players
    del players[:]
    #append ordered dicts to players list
    with open(players_file, 'r') as csv_file:
        for line in csv.DictReader(csv_file, fieldnames=('name', 'number', 'status')):
            players.append(dict(line))

#display list of players as they come in
def display_available_players(players: list, players_file: str):
    timeout = 5
    t = Timer(timeout, display_available_players, args=(players, players_file))
    t.start()
    retrieve_players(players, players_file)
    os.system('cls')
    if players: #if there are any players
        for player in players:
            #### THIS PRINTS TO THE SCREEN ####
            if player: #removes last empty line
                print('***\t'+player['name'])
    else: 
        print("No players have joined the game yet.")
    answer = input("***")
    t.cancel()
    if answer:
       print("***\tEveryone has joined! Looks like we're ready to play.")

print('on to the next thing!')

def add_player_answer(message_body: str, answers_file: str):
    with open(answers_file, 'a') as text_doc:
        text_doc.write(message_body+'\n')

# with open('answers.txt', 'a') as text_doc:
#     text_doc.write('\n')