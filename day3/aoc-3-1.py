#!/usr/bin/python
# This is the solution to part one of Advent of Code, day 3. 

f = open("input.txt",'r')
lines = list(f)
f.close()

patches = []

for line in lines:
  temp = line.split()
  startstr = temp[2]
  dimstr = temp[3]

  startstr = startstr[:-1]
  coords = [int(x) for x in startstr.split(",")]
  dims = [int(x) for x in dimstr.split("x")]

  ends = [a+b-1 for a,b in zip(coords,dims)]

  patches.append([coords,ends])

patches.sort()

# takes two (x1,y1),(x2,y2) defining upper left and lower right corners of squares
# returns upper left (x,y) and lower right (w,z) of intersection of them
def compute_intersection(pair1,pair2):
  x1 = pair1[0][0]
  y1 = pair1[0][1]
  x2 = pair1[1][0]
  y2 = pair1[1][1]

  u1 = pair2[0][0]
  v1 = pair2[0][1]
  u2 = pair2[1][0]
  v2 = pair2[1][1]

  output = []

  if u1 > x2:
    return [-1] 
  elif v1 > y2 or v2 < y1:
    return output
  elif y1 > v1:
    output.append([u1,y1])
    output.append([min(u2,x2),min(y2,v2)])
  else:
    output.append([u1,v1])
    output.append([min(x2,u2),min(v2,y2)])
  return output

points = set()

def add_points(pair,pointset):
  startx = pair[0][0]
  starty = pair[0][1]
  endx = pair[1][0]
  endy = pair[1][1]

  for i in range(startx,endx+1):
    for j in range(starty,endy+1):
      pointset.add((i,j))

for i in range(len(patches)):
  for j in range(i+1,len(patches)):
    intersection = compute_intersection(patches[i],patches[j])
    if -1 in intersection:
      break
    if intersection:
      add_points(intersection,points)

print(len(points))
