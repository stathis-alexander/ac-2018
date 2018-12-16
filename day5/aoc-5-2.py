#!/usr/bin/python
# This is a solution to part 2 of Advent of Code, day 5. 

f = open("input.txt","r")
polymerinput = f.read()
polymerinput = polymerinput[:-1]
f.close()

def react(polymerstring):
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
  return polymerstring

shortestlength = -1

for char in "abcdefghijklmnopqrstuvwxyz":
  polymerstr = polymerinput[:]
  polymerstr = polymerstr.replace(char,"")
  polymerstr = polymerstr.replace(char.upper(),"")

  editedpolymer = react(polymerstr)
  
  if (shortestlength == -1) or (len(editedpolymer) < shortestlength):
    shortestlength = len(editedpolymer)

print(shortestlength)
