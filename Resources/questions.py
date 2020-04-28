from random import randint

#finds num of lines in the questions doc
def find_num_of_lines(file: str) -> int:
    with open(file, 'r') as lines:
        total_lines = lines.readlines()
        return len(total_lines)

#gets a random question from list and appends that number to used_questions list
def get_random_question(file: str, num_of_questions: int, used_questions: list) -> str:
    with open(file, 'r') as questions:
        random_num = randint(0, num_of_questions-1)
        while random_num in used_questions:
            random_num = randint(0, num_of_questions-1)
        used_questions.append(random_num)
        lines = questions.readlines()
        return lines[random_num].strip()