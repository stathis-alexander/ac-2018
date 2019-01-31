#!/usr/bin/python
#This is a solution to Advent of Code, day 17 part 1.

import sys

if len(sys.argv) == 1:
  filename = "input.txt"
else:
  filename = sys.argv[1]

with open(filename,"r") as f:
  lines = [x.rstrip("\n") for x in f.readlines()]

cols = []
rows = []

for line in lines:
  parts = line.split(", ")

  pieces = parts[0].split("=")
  letter = pieces[0]
  num = int(pieces[1])

  if pieces[0] == "x":
    run = parts[1].lstrip("y=").split("..")
    cols.append([num,[int(run[0]),int(run[1])]])
  else:
    run = parts[1].lstrip("x=").split("..")
    rows.append([num,[int(run[0]),int(run[1])]])

grid = {(500,0):"+"}
for col in cols:
  colnum = col[0]
  for i in range(col[1][0],col[1][1]+1):
    grid[(colnum,i)] = "#"

for row in rows:
  rownum = row[0]
  for i in range(row[1][0],row[1][1]+1):
    grid[(i,rownum)] = "#"

def print_grid(grid):
  maxcol = max([col[0] for col in cols]+[row[1][1] for row in rows])+2
  maxrow = max([row[0] for row in rows]+[col[1][1] for col in cols])+2
  for i in range(maxrow):
    for j in range(maxcol):
      if (j,i) not in grid:
        print(".",end="")
      else:
        print(grid[(j,i)],end="")
    print()


def flow_water(pair,over):
  down = pair + (0,1)
  left = pair + (-1,0)
  right = pair + (1,0)

  if down in grid:
    if left not in grid:
      l = flow_water(left)
    else:
      return 1
    if right not in grid:
      r = flow_water(right)
    else:
      return 1
  else:
    grid[down] = "|"
    return 1 + flow_water(down)


print_grint(grid)
