# defining function to add a player to the group
import csv

def add_player(message_body, number):
    with open('players.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)

with open("temp.txt") as file:
    print(file.readline())

# def add_player(message_body, number):
# with open('eggs.csv', 'w') as csvfile:
#     csv_writer = csv.writer(csvfile, delimiter=',')
#     csv_writer.writerow(['yes', 'no'])


    # if not any(player['number'] == number for player in players):
    #     players.append({'player': message_body, 'number': number})
    # else: 
    #     print("This user has already been added")
