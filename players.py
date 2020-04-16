import csv
import os

################################
## ADDS PLAYER TO PLAYERS.CSV ##
################################

#checking if incoming number already exists in the player file. 
#!!!! currently doesn't work
def check_number_player(incoming_number: str, players_file: str) -> str:
    with open(players_file, 'r') as csv_file:
        for line in csv.DictReader(csv_file, fieldnames=('name', 'number', 'status')):
            if incoming_number == line['number']:
                return ''
            return incoming_number

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
    retrieve_players(players, players_file)
    os.system('cls')
    print('*'*70 * 4 + '\n')
    if players: #players contains any value
        for player in players:
            if player: #remove any empty lines
                print('\t\t'+player['name'])
    else:
        print('\t\t'+"No players have joined the game yet.")

def add_player_answer(message_body: str, answers_file: str):
    with open(answers_file, 'a') as text_doc:
        text_doc.write(message_body+'\n')
