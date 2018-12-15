#!/usr/bin/python
# This solves puzzle two of Advent of Code, Day 2.

f = open('input.txt','r')

freq = 0
freqlist = list(f)
f.close()

freqset = {0}

i = 0
while i < len(freqlist):

  if freqlist[i][0] == '+':
    freq += int(freqlist[i][1:])
  else:
    freq -= int(freqlist[i][1:])
  if freq in freqset:
      break
  else:
      freqset.add(freq)

  i += 1
  if i == len(freqlist):
      i = 0

print(freq)
f.close()
