#!/usr/bin/python
# This is a solution to Advent of Code, day 9 part 1.

with open("input.txt","r") as f:
  data = f.read().rstrip("/n").split()

no_players = int(data[0])
last_marble = int(data[6])

players = [0] * no_players
game = [0]

last_played = 0

for i in range(1,last_marble+1):
  if i % 23 == 0:
    players[i%no_players] += i
    next_play = (last_played - 7) % len(game)

    if next_play < 0:
      next_play += len(game)

    players[i%no_players] += game.pop(next_play)
  else:
    next_play = last_played+2 % len(game)
    game.insert(next_play,i)

  last_played = next_play

print(max(players))

