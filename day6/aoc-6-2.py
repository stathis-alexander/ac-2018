#!/usr/bin/python
# This is a solution to Advent of Code, day 6 part 2

with open("input.txt","r") as f:
  coordlist = [tuple([int(x) for x in line.rstrip("\n").split(", ")]) for line in list(f)]

xes = [x[0] for x in coordlist]
yes = [x[1] for x in coordlist]

x_small = min(xes)
x_big = max(xes)
y_small = min(yes)
y_big = max(yes)

def compute_weight(u,v):
  weight = 0

  for coord in coordlist:
    weight += abs(coord[1] - v) + abs(coord[0] - u)
  
  return weight

good_set = set()

for u in range(x_small,x_big+1):
  for v in range(y_small,y_big+1):
    weight = compute_weight(u,v)
    if weight < 10000:
      good_set.add((u,v))    


print(len(good_set))
