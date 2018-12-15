#!/usr/bin/python
# this solves puzzle one of Advent of Code, Day 1.


f = open('input.txt','r')

freq = 0

for line in f:
	if line[0] == '+':
	    freq += int(line[1:])
	else:
	    freq -= int(line[1:])
	
f.close()

print(freq)
