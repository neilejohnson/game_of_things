import csv
from answers import add_answer
from pathlib import Path

msg = 'neil'
num = '757'
answers_file=str(Path(__file__).parent)+'\\Data\\answers.csv'
print(answers_file)

add_answer(msg, num, answers_file)