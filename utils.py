import csv


def read_single_column_ints_csv(filename):
    rows = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            rows.append(int(row[0]))

    return rows


def read_single_column_csv(filename):
    rows = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            rows.append(row[0])

    return rows