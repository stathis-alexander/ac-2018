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

  if u1 > x2 or v1 > y2 or v2 < y1:
    return output
  elif y1 > v1:
    output.append([u1,y1])
    output.append([min(u2,x2),min(y2,v2)])
  else:
    output.append([u1,v1])
    output.append([min(x2,u2),min(v2,y2)])
  return output

intersected = False
winner = -1

for i in range(len(patches)):
  for j in range(len(patches)):
    if i < j:
      intersection = compute_intersection(patches[i],patches[j])
    elif i == j:
      continue
    else:
      intersection = compute_intersection(patches[j],patches[i])
    if intersection:
      intersected = True
      break
  if not intersected:
    print(i)
    winner = i
  else:
    intersected = False

for line in lines:
  temp = line.split()
  startstr = temp[2]
  dimstr = temp[3]

  startstr = startstr[:-1]
  coords = [int(x) for x in startstr.split(",")]
  dims = [int(x) for x in dimstr.split("x")]

  ends = [a+b-1 for a,b in zip(coords,dims)]

  if coords[0] == patches[winner][0][0] and coords[1] == patches[winner][0][1] and ends[0] == patches[winner][1][0] and ends[1] == patches[winner][1][1]:
    print(temp[0])
