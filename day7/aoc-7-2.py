#!/usr/bin/python
# This is a solution to Advent of Code, day 7 part 2. 

with open("input.txt","r") as f:
  dependencies = [(line[5],line[36]) for line in f.readlines()]

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

node_table = dict(zip(letters,[[] for x in range(26)]))

for depends in dependencies:
  first = depends[0]
  second = depends[1]  

  node_table[first].append(second)

heads = []
processing = []
processed = []

for letter in letters:
  if(not any([letter in node_table[key] for key in node_table])):
    heads.append(letter)


for node in node_table:
  print(node,":",node_table[node])

time = 0
workers = [["",0],["",0],["",0],["",0],["",0]]

def working(workers):
  if any([worker[1] >= 0 for worker in workers]) or heads:
    return True
  else:
    return False

while working(workers):
  print("time",time,":",heads,"::",workers)

  # unload any processed
  for worker in workers:
    if worker[0] and worker[1] == 0: 
      head = worker[0]
      processing.remove(head)
      processed.append(head)
      for x in node_table[head]:
        print("time",time,":",head,x)
        if(x not in processing and not any([(key not in processed) and (x in node_table[key]) for key in node_table])):
          heads.append(x)
      worker[0] = ""

  heads.sort(reverse=True)

  for worker in workers:
    if worker[1] <= 0 and heads:  
      head = heads.pop()
      processing.append(head)
      worker[0] = head
      worker[1] = ord(head)-4
  
  heads = list(set(heads))

  time += 1

  for worker in workers:
    worker[1] -= 1

time -= 1

print(''.join(processed),"in time",time)
