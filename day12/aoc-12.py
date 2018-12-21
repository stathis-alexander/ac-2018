#!/usr/bin/python
# This is a solution to Advent of Code, day 12 part 1 and part 2.

with open("input.txt","r") as f:
  start_state = f.readline().rstrip("\n").lstrip("initial state: ")
  f.readline()
  rules_lines = [line.rstrip("\n") for line in f.readlines()]

zero = 2000

state = "." * zero
state = state + start_state + state

rules = {}

for rule in rules_lines:
  parts = rule.split(" => ")
  rules[parts[0]] = parts[1]

generations = 500 
for generation in range(generations+1):
  new_state = ".."
  for i in range(2,len(state)-2):
    sub = state[i-2:i+3]
    if sub in rules:
      new_state += rules[sub]
    else:
      new_state += "."
  new_state = new_state + ".."
  state = new_state

pots_sum = 0
for i in range(len(state)):
  if state[i] == "#":
    pots_sum += (i - zero)
print(generations,":",pots_sum)

print(5115 + 26 * (171-170))
print(5115 + 26 * (49999999999-170))

# the pattern stabilizes around 160/170 generations and then just becomes a shift by 26. 
