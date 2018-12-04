import re
from utils import read_single_column_csv


class GuardEvent(object):
    def __init__(self, data):
        regex = '\[(?P<timestamp>.*)\]\s(?P<action>falls asleep|wakes up|Guard #(?P<guard_id>\d+) begins shift)'
        values = re.match(regex, data)

        timestamp_regex = '(?P<year>\d+)\-(?P<month>\d+)\-(?P<day>\d+)\s(?P<hours>\d+):(?P<minutes>\d+)'
        self.timestamp = values.group('timestamp')
        timestamp_values = re.match(timestamp_regex, self.timestamp)
        self.year = int(timestamp_values.group('year'))
        self.month = int(timestamp_values.group('month'))
        self.day = int(timestamp_values.group('day'))
        self.hours = int(timestamp_values.group('hours'))
        self.minutes = int(timestamp_values.group('minutes'))

        self.action = values.group('action')
        if values.group('guard_id'):
            self.guard_id = int(values.group('guard_id'))
        else:
            self.guard_id = 0

    def get_day_string(self):
        return '{}-{}-{}'.format(self.year, self.month, self.day)

    def is_asleep(self):
        return self.action == 'falls asleep'

    def is_awake(self):
        return self.action == 'wakes up'

    def is_guard_change(self):
        return not (self.is_awake() or self.is_asleep())

    def get_guard_id(self):
        return self.guard_id

    def __str__(self):
        return '{}: {}'.format(self.timestamp, self.action)


class GuardSleepData(object):
    def __init__(self, guard_id):
        self.guard_id = guard_id
        self.total_sleep = 0
        self.sleep = [0 for minute in range(60)]

    def add_sleep(self, from_minute, to_minute):
        for min in range(to_minute-from_minute):
            self.sleep[from_minute+min] += 1
            self.total_sleep += 1

    def get_minute_with_max_sleep(self):
        max_sleep = max(self.sleep)
        return self.sleep.index(max_sleep)

    def get_max_sleep(self):
        return max(self.sleep)


# just use some fake delimiter to capture the whole line
data = read_single_column_csv('task4_input.csv', delimiter='$')
all_events = []
for guard_data in data:
    guard_event = GuardEvent(guard_data)
    all_events.append(guard_event)

all_events.sort(key=lambda event: event.timestamp)
guard_dict = {}

guard_id = None
sleep_start = None
sleep_end = None
for event in all_events:
    if event.is_guard_change():
        guard_id = event.get_guard_id()
    if event.is_asleep():
        sleep_start = event.minutes
    if event.is_awake():
        sleep_end = event.minutes
        guard_sleep_data = guard_dict.get(guard_id)
        if not guard_sleep_data:
            guard_sleep_data = GuardSleepData(guard_id)
            guard_dict[guard_id] = guard_sleep_data
        guard_sleep_data.add_sleep(sleep_start, sleep_end)

guard_with_max_sleep = None
for key, guard_sleep_data in guard_dict.iteritems():
    if not guard_with_max_sleep:
        guard_with_max_sleep = guard_sleep_data
        continue

    if guard_sleep_data.total_sleep > guard_with_max_sleep.total_sleep:
        guard_with_max_sleep = guard_sleep_data

print 'Guard ID with most sleep = {}'.format(guard_with_max_sleep.guard_id)
print 'Guard slept most at minute = {}'.format(guard_with_max_sleep.get_minute_with_max_sleep())
print 'Answer guard_id * minute_with_most_sleep = {}'.format(
    guard_with_max_sleep.guard_id * guard_with_max_sleep.get_minute_with_max_sleep()
)


# Part two
guard_with_most_sleepy_minute = None
for key, guard_sleep_data in guard_dict.iteritems():
    if not guard_with_most_sleepy_minute:
        guard_with_most_sleepy_minute = guard_sleep_data
        continue

    if guard_sleep_data.get_max_sleep() > guard_with_max_sleep.get_max_sleep():
        guard_with_most_sleepy_minute = guard_sleep_data


print 'Guard ID with most sleepy minute = {}'.format(guard_with_most_sleepy_minute.guard_id)
print 'Guard slept most at minute = {} {} times'.format(
    guard_with_most_sleepy_minute.get_minute_with_max_sleep(),
    guard_with_most_sleepy_minute.get_max_sleep()
)
print 'Answer guard_id * minute_with_most_sleep = {}'.format(
    guard_with_most_sleepy_minute.guard_id *
    guard_with_most_sleepy_minute.get_minute_with_max_sleep()
)
