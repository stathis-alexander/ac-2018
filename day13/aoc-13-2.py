#!/usr/bin/python
# This is a solution to Advent of Code, day 13 part 2.

grid = []

with open("input4.txt","r") as f:
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
  for j in range(len(grid[i])):
    if grid[i][j] in move_table:
      carts.append([i,j,grid[i][j],0])

tick = 0

while len(carts) > 1:

  tick += 1
  carts.sort()

  i = 0
  while i < len(carts):
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

    for j in range(len(carts)):
      if i != j and carts[i][0] == carts[j][0] and carts[i][1] == carts[j][1]:
        carts.pop(max(j,i))
        carts.pop(min(j,i))
        if i > j:
          i -= 1
        i -= 1
        break
    i +=1

print(carts[0][1],carts[0][0])
