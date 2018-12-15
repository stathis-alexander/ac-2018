#!/usr/bin/python
# this is a solution to part 1 of Advent of Code, day 2.

f = open("input.txt", "r")
lines = list(f)
f.close()

twos = 0
threes = 0

for l in lines:
  line = list(l)
  line.sort()
  
  i = 0
  j = 1
  
  twice = False
  thrice = False
  
  while j < len(line):
    while j < len(line) and line[i] == line[j]:
      j += 1
    if j - i == 2 and not twice:
      twos += 1
      twice = True
    elif j - i == 3 and not thrice:
      threes += 1
      thrice = True
    i = j
    j = i+1
    
print(twos * threes)