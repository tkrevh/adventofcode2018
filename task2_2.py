from utils import read_single_column_csv


def different_in_one_letter_only(word1, word2):
    diffs = 0
    diff_at = 0
    for i, c in enumerate(word1):
        if c != word2[i]:
            diffs += 1
            diff_at = i
        if diffs > 1:
            return False, diff_at

    return True, diff_at


all_words = read_single_column_csv('task2_input.csv')
for index, word1 in enumerate(all_words):
    rest_of_words = all_words[index+1:]
    for word2 in rest_of_words:
        diff, index = different_in_one_letter_only(word1, word2)
        if diff:
            print 'Found correct words {} and {}, diff at index {}'.format(word1, word2, index)
            common_letters = word1[:8]+word1[9:]
            print 'Common letters are {}'.format(common_letters)

