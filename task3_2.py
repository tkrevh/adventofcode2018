import re
from utils import read_single_column_csv


class ClaimData(object):
    def __init__(self, canvas_claim, sum):
        self.canvas_claims = [canvas_claim]
        self.sum = sum

    def add_claim(self, canvas_claim):
        self.canvas_claims.append(canvas_claim)
        self.inc()
        for canvas_claim in self.canvas_claims:
            canvas_claim.overlaps += 1

    def inc(self):
        self.sum += 1


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
        self.overlaps = 0

    def claim_canvas(self, canvas):
        for y in range(self.height):
            for x in range(self.width):
                claim_data = canvas[self.y + y][self.x + x]
                if not claim_data:
                    claim_data = ClaimData(self, 0)
                    canvas[self.y + y][self.x + x] = claim_data
                else:
                    claim_data.add_claim(self)


# just use some fake delimiter to capture the whole line
data = read_single_column_csv('task3_input.csv', delimiter='$')
canvas_width, canvas_height = 1000, 1000
canvas = [[None for x in range(canvas_width)] for y in range(canvas_height)]

all_claims = []
for claim_data in data:
    canvas_claim = CanvasClaim(claim_data)
    canvas_claim.claim_canvas(canvas)
    all_claims.append(canvas_claim)

for claim in all_claims:
    if claim.overlaps == 0:
        print 'Found claim with 0 overlaps:{}'.format(claim.id)
