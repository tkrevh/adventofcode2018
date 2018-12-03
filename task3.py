import re
from utils import read_single_column_csv


class CanvasClaim(object):
    def __init__(self, data):
        # data has the following format #1 @ 555,891: 18x12
        regex = '#(?P<id>\d+)\s@\s(?P<x>\d+),(?P<y>\d+):\s(?P<width>\d+)x(?P<height>\d+)'
        values = re.match(regex, data)
        self.id = int(values.group('id'))
        self.x = int(values.group('x'))
        self.y = int(values.group('y'))
        self.width = int(values.group('width'))
        self.height = int(values.group('height'))

    def claim_canvas(self, canvas):
        for y in range(self.height):
            for x in range(self.width):
                canvas[self.y + y][self.x + x] += 1


# just use some fake delimiter to capture the whole line
data = read_single_column_csv('task3_input.csv', delimiter='$')
canvas_width, canvas_height = 1000, 1000
canvas = [[0 for x in range(canvas_width)] for y in range(canvas_height)]

for claim_data in data:
    canvas_claim = CanvasClaim(claim_data)
    canvas_claim.claim_canvas(canvas)

overlap = 0
for y in range(canvas_height):
    for x in range(canvas_width):
        if canvas[y][x] > 1:
            overlap += 1

print overlap