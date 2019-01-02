#!/usr/bin/python
# This is a solution to Advent of Code, day 15 part 1. 

import sys, copy

class Warrior:
  def __init__(self,pos):
    if pos is Warrior:
      self.hp = pos.hp
      self.pos = pos.pos
    else:
      self.hp = 200
      self.pos = pos

if len(sys.argv) == 1:
  inputfile = "input.txt"
else:
  inputfile = sys.argv[1]

with open(inputfile,"r") as f:
  lines = [x.rstrip("\n") for x in f.readlines()]

size = len(lines)

goblins = []
elves = []
grid = {}

i = 0
j = 0

for line in lines:
  for x in line:
    if x == "E":
      elf = Warrior((i,j))
      elves.append(elf)
    elif x == "G":
      goblin = Warrior((i,j))
      goblins.append(goblin)
    grid[(i,j)] = x
    j+=1
  j=0
  i+=1

def adjacent(source):
  return [tuple(map(sum, zip(source, x))) for x in [(-1,0),(0,-1),(0,1),(1,0)]]

def dijkstras(combatant):
  start = combatant.pos
  queue = [start]

  considered = set()

  prev = {start: None}
  dist = {start: 0}

  while queue:
    queue.sort(reverse=True,key=lambda pair:dist[pair])
    consider = queue.pop()
    for adj in adjacent(consider):
      if adj not in dist or dist[adj] > dist[consider] + 1 or ((dist[adj] == dist[consider] + 1) and (consider < prev[adj])):
        dist[adj] = dist[consider] + 1      
        prev[adj] = consider
      if (adj not in considered) and (adj not in queue) and (grid[adj] == "."):
        queue.append(adj) 
    considered.add(consider)

  return dist, prev   

def print_grid(grid):
  for i in range(size):
    for j in range(size):
      if (i,j) in grid:
        print(grid[(i,j)],end="")
      else:
        print(end=" ")
    print()

def find_move(prev, square):
  while prev[prev[square]]:
    square = prev[square]
  return square

def find_lowest_hp_neighbor(warrior):
  warrior_type = grid[warrior.pos]
  min_hp = 500
  victim = Warrior((255,255))
  for x in adjacent(warrior.pos):
    if grid[x] in "EG" and grid[x] != grid[warrior.pos]:
      for fighter in elves + goblins:
        if fighter.pos == x and (fighter.hp < min_hp or (fighter.hp == min_hp and fighter.pos < victim.pos)):
          min_hp = fighter.hp
          victim = fighter
  return victim

def kill(victim):
  if grid[victim.pos] == "E":
    elves.remove(victim)
  elif grid[victim.pos] == "G":
    goblins.remove(victim)
  grid[victim.pos] = "."

print("Input File:",inputfile)
print_grid(grid)

i = 31
turn = 0
while goblins and elves:
  turn += 1
  combatants = sorted(goblins + elves, key=lambda warrior: warrior.pos)

  for warrior in combatants:
    if warrior in elves:
      targets = goblins
    elif warrior in goblins:
      targets = elves
    else:
      continue

    in_range = []
    for target in targets:
      for consider in adjacent(target.pos):
        if consider in grid and grid[consider] in ".EG":
          in_range.append(consider)
    
    if not in_range:
      continue

    if warrior.pos not in in_range:
      dist, prev = dijkstras(warrior)
      directions = []
      directions = sorted([square for square in in_range if (square in dist and grid[square] not in "EG#")],reverse=True,key=lambda pair:dist[pair])
      if not directions: 
        continue
     
      moves = sorted([x for x in directions if dist[x] == dist[directions[len(directions)-1]]],reverse=True)
      move = find_move(prev,moves.pop())

      grid[move] = grid[warrior.pos]
      grid[warrior.pos] = "."
      warrior.pos = move

    if warrior.pos in in_range:
      victim = find_lowest_hp_neighbor(warrior)
      if grid[victim.pos] == "E":
        victim.hp -= 3
      else:
        victim.hp -= (3 + i)
      if victim.hp <= 0:
        kill(victim)

print("End of Turn:",turn,"and i =",i)
print_grid(grid)
  
print("Elves:")
for x in elves:
  print(x.pos,":",x.hp)
  
print("Goblins:")
for x in goblins:
  print(x.pos,":",x.hp)

total = sum([x.hp for x in elves + goblins])

print(total,"*",turn,"=",total * turn)


