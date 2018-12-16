#!/usr/bin/python
# This is a solution to part 2 of Advent of Code, day 5. 

f = open("input.txt","r")
polymerstring = f.read()
polymerstring = polymerstring[:-1]
f.close()

i = 0
while i < len(polymerstring)-1:
  char = polymerstring[i]
  nextchar = polymerstring[i+1]
  if (char.isupper() and char.lower() == nextchar) or (char.islower() and char.upper() == nextchar):
    polymerstring = polymerstring[:i] + polymerstring[i+2:]
    if i != 0:
      i -= 1
  else:
    i += 1


print(len(polymerstring))
