import re
from utils import read_lines

def react_polymer(string):
    line_list = list(string)
    duplicates_found = True
    while duplicates_found:
        duplicates_found = False
        for index in range(len(line_list)-1):
            c1 = line_list[index]
            c2 = line_list[index+1]
            if c1 and c2 and abs(ord(c1) - ord(c2)) == 32:
                line_list[index] = ''
                line_list[index+1] = ''
                duplicates_found = True
        if duplicates_found:
            line_list = list("".join(line_list))

    return "".join(line_list)


data = read_lines('task5_input.txt')
string = data[0]
# Task 1
result = react_polymer(string)
print 'Remains: {}'.format(result)
print 'Remain length: {}'.format(len(result))

# Task 2
results = {}
for c in range(ord('Z') - ord('A')):
    c1 = chr(65+c)
    c2 = chr(97+c)
    regex = c1
    search_string = re.sub(c1, '', string)
    search_string = re.sub(c2, '', search_string)
    results['{}{}'.format(c1, c2)] = react_polymer(search_string)

for key,value in results.iteritems():
    print 'Removed {} produced {} length polymer'.format(key, len(value))