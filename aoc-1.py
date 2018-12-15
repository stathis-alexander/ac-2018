#!/usr/bin/python

f = open('input.txt','r')

freq = 0

for line in f:
	if line[0] == '+':
	    freq += int(line[1:])
	else:
	    freq -= int(line[1:])
	
f.close()

print(freq)
