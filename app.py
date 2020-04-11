import csv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from players import add_player, add_player_answer, check_number_player
from random import randint
from answers import check_number_answer, add_answer
from pathlib import Path

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def save_message():

########################
### define variables ###
########################

    number = request.form['From']
    message_body = request.form['Body']

    data_path = str(Path(__file__).parent)+'\\Data\\'
    temp_file = data_path+'temp.txt'

##################################################
### check for game master's 'start' or 'force' ###
##################################################

    #initiatiate start of game - if any player texts 'start' to number, the game moves forward.
    if message_body.lower() == 'start':
        with open(temp_file, "w") as temp:
            temp.write("game")
    
    #forces end of answer phase - while force the round to move forward if someone is sitting out the round
    elif message_body.lower() == 'force':
        with open(temp_file, "w") as temp:
            temp.write("reframe")
            return 'force start'

###################################
### add response to answers.csv ###
###################################
    
    #identifies environmental variable
    with open(temp_file, "r") as temp:
       environment = temp.readline()

    #adds player to csv if environment is 'name'
    if environment != 'name':
        answers_file = data_path+'answers.csv'
        # !!!! this probably doesn't work. check back later
        #number = check_number_answer(number, answers_file)
        if number:
            add_answer(message_body, number, answers_file)
            return '{} has submitted a response. - {}'.format(number, message_body)
        return '{} has already submitted a response.'.format(number)

###################################
### add response to players.csv ###
###################################

    else:
        players_file = data_path + 'players.csv'
        #if player's number has already been used, do not accept. !!!! Currently doesn't work
        #number = check_number_player(number, players_file) 
        if number:
            add_player(message_body, number, players_file)
            print('added player')
            return '{} has joined the game.'.format(message_body)
        print('nope')
        return '{} has already submitted a response'.format(number)

    return number, message_body

if __name__ == "__main__":
    app.run(debug=True)