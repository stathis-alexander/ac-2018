#!/usr/bin/python
# This is a solution to Advent of Code, day 9 part 1.

with open("input.txt","r") as f:
  data = f.read().rstrip("/n").split()

players = int(data[0])
last_marble = int(data[6])

print(players,last_marble)
