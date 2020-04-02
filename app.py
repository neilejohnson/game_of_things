import csv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from players import add_player, add_player_answer
from random import randint
from pathlib import Path

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def save_message():
    #retreive user input
    number = request.form['From']
    message_body = request.form['Body']

    data_path = str(Path(__file__).parent)+'\\Data\\'

    #if message = start then we pause for the until we 
        #environment == game

    #if number has already been used within answer or names, do not accept

    #identifies environmental variable
    with open(data_path+'temp.txt', "r") as temp:
       environment = temp.readline() 

    #adds player to csv if environment is 'name'wor
    if environment != 'name':
        answers_file = data_path+'answers.txt'
        with open(answers_file, 'a') as text_doc:
            text_doc.write(message_body+'\n')

    #else add incoming answer to txt document
    else:
        players_file = data_path + 'players.csv'
        add_player(message_body, number, players_file)
        return '{} has joined the game.'.format(message_body)

    return number, message_body

if __name__ == "__main__":
    app.run(debug=True)