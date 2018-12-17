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

def find_nearest(u,v):
  disttonear = 1000
  nearest = None
  unique_nearest = True

  for coord in coordlist:
    distance = abs(coord[1] - v) + abs(coord[0] - u)
    if distance < disttonear:
      unique_nearest = True
      nearest = coord
      disttonear = distance
    elif distance == disttonear:
      unique_nearest = False
  
  return unique_nearest,nearest,disttonear

def on_boundary(u,v):
  if u in [x_small,x_big] or v in [y_small,y_big]:
    return True
  else:
    return False

infinite_set = set()
areas = dict(zip(coordlist,[0]*len(coordlist)))

for u in range(x_small,x_big+1):
  for v in range(y_small,y_big+1):
    [unique,nearest,distance] = find_nearest(u,v)
    
    if not unique or nearest in infinite_set:
      continue
    elif on_boundary(u,v):
      infinite_set.add(nearest)
      areas[nearest] = 0
    else:
      areas[nearest] = areas[nearest] + 1

print(max([areas[item] for item in areas]))

