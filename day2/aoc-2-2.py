#!/usr/bin/python
# this is a solution to part 2 of Advent of Code, day 2.

f = open("input.txt", "r")
lines = list(f)
f.close()

for i in range(len(lines)):
  for j in range(i+1,len(lines)):
    
    differencefound = -1
    
    for k in range(len(lines[i])):
      if lines[i][k] != lines[j][k] and differencefound < 0:
        differencefound = k
      elif lines[i][k] != lines[j][k] and differencefound >= 0:
        differencefound = -1
        break
    
    if differencefound >= 0:
      print(lines[i][:differencefound]+lines[i][differencefound+1:])
      break
    
  
