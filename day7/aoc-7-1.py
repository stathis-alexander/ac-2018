#!/usr/bin/python
# This is a solution to Advent of Code, day 7 part 1. 

with open("input.txt","r") as f:
  dependencies = [(line[5],line[36]) for line in f.readlines()]

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

node_table = dict(zip(letters,[[] for x in range(26)]))

for depends in dependencies:
  first = depends[0]
  second = depends[1]  

  node_table[first].append(second)

heads = []
seen = []

for letter in letters:
  if(not any([letter in node_table[key] for key in node_table])):
    heads.append(letter)

for key in node_table:
  print(key,":",node_table[key])

while heads:
  heads.sort(reverse=True)
  head = heads.pop()

  print(head,heads)

  if head in seen:
    continue
  else:
    seen.append(head)
  for x in node_table[head]: 
    if(not any([(key not in seen) and (x in node_table[key]) for key in node_table])):
      heads.append(x)
  
  heads = list(set(heads))

print(''.join(seen))
