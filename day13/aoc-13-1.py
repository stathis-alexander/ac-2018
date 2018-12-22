#!/usr/bin/python
# This is a solution to Advent of Code, day 13 part 1.

grid = []

with open("input.txt","r") as f:
  grid = [list(line.rstrip("\n")) for line in f.readlines()]

carts = []

move_table = {
  "<": [0,-1],
  ">": [0,1],
  "^": [-1,0],
  "v": [1,0]
  }

resolve_move = {
  "/"+">": "^",
  "/"+"^": ">",
  "/"+"<": "v",
  "/"+"v": "<",
  "\\"+">": "v",
  "\\"+"^": "<",
  "\\"+"<": "^",
  "\\"+"v": ">"
  }

intersection = {
  ">"+str(0): "^",
  ">"+str(1): ">",
  ">"+str(2): "v",
  "^"+str(0): "<",
  "^"+str(1): "^",
  "^"+str(2): ">",
  "v"+str(0): ">",
  "v"+str(1): "v",
  "v"+str(2): "<",
  "<"+str(0): "v",
  "<"+str(1): "<",
  "<"+str(2): "^"
  }

for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] in move_table:
      carts.append([i,j,grid[i][j],0])

carts.sort()
print(carts)

crash_location = []

crash = False
while not crash:
  for i in range(len(carts)):
    cart = carts[i]
    
    x = cart[0]
    y = cart[1]
    cart_type = cart[2]
    last_move = cart[3]

    x += move_table[cart_type][0]
    y += move_table[cart_type][1]

    if grid[x][y] in "\\/":
      cart_type = resolve_move[grid[x][y]+cart_type]
    elif grid[x][y] == "+":
      cart_type = intersection[cart_type+str(last_move)]
      last_move = (last_move + 1) % 3

    carts[i] = [x,y,cart_type,last_move]
    print(carts[i])
  
  for i in range(len(carts)):
    for j in range(i+1,len(carts)):
      if carts[i][0] == carts[j][0] and carts[i][1] == carts[j][1]:
        crash = True
        crash_location = [carts[i][1],carts[i][0]]

print(crash_location)
