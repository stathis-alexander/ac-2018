#!/usr/bin/python
# this is a solution to part 2 of Advent of Code, day 4

from datetime import datetime

f = open("input.txt","r")
lines = list(f)
f.close()

data = []

for line in lines:
  [datestr,actionstr] = line.split("]")
  datestr = datestr[1:]
  actionstr = actionstr[1:-1]

  timestamp = datetime.strptime(datestr, "%Y-%m-%d %H:%M")

  data.append([timestamp,actionstr])

data.sort()

guards = {}
current_guard_no = -1
sleep_minute = -1

for datum in data:
  if datum[1] == "falls asleep":
    sleep_minute = int(datum[0].minute)
  elif datum[1] == "wakes up":
    if current_guard_no not in guards:
      guards[current_guard_no] = [[sleep_minute,datum[0].minute]]
    else: guards[current_guard_no].append([sleep_minute,datum[0].minute])
  else:
    pieces = datum[1].split()
    pieces[1] = pieces[1][1:]
    current_guard_no = int(pieces[1])

minute = -1
freq = 0
guardno = -1

for guard in guards:
  for i in range(60):
    counter = 0
    for pair in guards[guard]:
      if pair[0] <= i and pair[1] > i:
        counter += 1
    if counter > freq:
      guardno = guard
      minute = i
      freq = counter

print(guardno,minute,guardno*minute)
