from utils import read_single_column_ints_csv

all_inputs = read_single_column_ints_csv('task1_input.csv')

result = 0
frequencies = {}
duplicate_found = False
while not duplicate_found:
    for input in all_inputs:
        result += input
        if frequencies.get(result):
            print result
            duplicate_found = True
            break
        else:
            frequencies[result] = result