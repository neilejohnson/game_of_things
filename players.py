import csv
import os
from time import sleep

################################
## ADDS PLAYER TO PLAYERS.CSV ##
################################

def check_number_player(incoming_number: str, players_file: str) -> str:
    with open(players_file, 'r') as csv_file:
        for line in csv.reader(csv_file):
            if line[1] == incoming_number:
                print('dismissed duplicate response')
                return ''
    print('returning number')
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

def add_player_answer(message_body: str, answers_file: str):
    with open(answers_file, 'a') as text_doc:
        text_doc.write(message_body+'\n')

#########################
## FIND WINNING PLAYER ##
#########################

def retreive_winning_player(answers: list, answers_file: str, players_file: str) -> str:
    winning_answer = answers[0][1]
    #dig into answer file first
    with open(answers_file, 'r') as csv_file:
        for line in csv.DictReader(csv_file, fieldnames=('answer', 'number')):
            if dict(line)['answer'] == winning_answer:
                winning_number = dict(line)['number']
    with open(players_file, 'r') as csv_file:
        for line in csv.DictReader(csv_file, fieldnames=('name', 'number', 'status')):
            if dict(line)['number'] == winning_number:
                winner_round = dict(line)['name']
    return winner_round
