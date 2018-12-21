#!/usr/bin/python
# This is a solution to Advent of Code, day 11 part 1.

import math

#the input for this one is not a file, but a number
starting_input = 1718

def power_level(i,j):
  power = 0

  rack = i + 10

  power = (rack * j + starting_input) * rack

  digit = math.floor(power/100) - math.floor(power/1000) * 10

  power = digit - 5

  return power

grid = [[0]*301]
big_power = -1
x_max = -1
y_max = -1

for i in range(1,301):
  grid.append([0])
  for j in range(1,301):
    grid[i].append(power_level(i,j))

for i in range(1,298):
  for j in range(1,298):
    cube_power = 0
    for u in range(0,3):
      for v in range(0,3):
        cube_power += grid[i+u][j+v]
    if cube_power > big_power:
      big_power = cube_power
      x_max = i
      y_max = j

print("(",x_max,",",y_max,"):", big_power)
