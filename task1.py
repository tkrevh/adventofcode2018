from utils import read_single_column_ints_csv

result = 0
for row in read_single_column_ints_csv('task1_input.csv'):
    result += row

print result
