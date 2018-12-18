#!/usr/bin/python
# This is a solution to Advent of Code, day 10 part 1.

with open("input.txt","r") as f:
  lines = [line.rstrip("\n") for line in f.readlines()]

points_list = []

for line in lines:
  pieces = line.lstrip("position=<").rstrip(">").split(", ")
  x_coord = int(pieces[0].strip())
  y_vec = int(pieces[2].strip())
  
  pieces_pieces = pieces[1].split("> velocity=<")

  x_vec = int(pieces_pieces[1].strip())
  y_coord = int(pieces_pieces[0].strip())
  
  points_list.append([[x_coord,y_coord],[x_vec,y_vec]])


for x in points_list:
  x[0][0] += x[1][0]*10081
  x[0][1] += x[1][1]*10081

# guessed the correct time by checking when the x_min, x_max stopped strictly descreasing, then halfed it. I think the proper way to do this
# would be to look for the time when the abs(x_min-x_max) and abs(y_min-y_max) was minimum 


points = set([tuple(x[0]) for x in points_list])

x_min = min([x[0][0] for x in points_list])
x_max = max([x[0][0] for x in points_list])

y_min = min([x[0][1] for x in points_list])
y_max = max([x[0][1] for x in points_list])

for i in range(y_max+1):
  for j in range(x_max+1):
    if (j,i) in points:
      print("X",end='')
    else:
      print(end=" ")
  print()
