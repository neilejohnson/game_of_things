import csv

#deletes contents of txt or csv files
def clear_file(file_to_clear: str):
    open(file_to_clear, 'w').close()

def dismiss_duplicate_response(incoming_number: str, csv_file: str) -> str:
    with open(csv_file, 'r') as csv_file:
        for line in csv.reader(csv_file):
            if line[1] == incoming_number:
                print('dismissed duplicate response')
                return ''
    print('returning number')
    return incoming_number