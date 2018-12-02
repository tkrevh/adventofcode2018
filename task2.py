from utils import read_single_column_csv


def letter_appears_two_or_three_times(word):
    d = {}
    for c in word:
        if d.get(c) is None:
            d[c] = 1
        else:
            d[c] += 1

    found_two = False
    found_three = False

    for key, value in d.iteritems():
        if value == 2:
            found_two = True
        if value == 3:
            found_three = True

    return found_two, found_three

found_twos = 0
found_threes = 0
for word in read_single_column_csv('task2_input.csv'):
    twos, threes = letter_appears_two_or_three_times(word)
    if twos:
        found_twos += 1
    if threes:
        found_threes += 1

print found_twos * found_threes