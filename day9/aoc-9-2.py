#!/usr/bin/python
# This is a solution to Advent of Code, day 9 part 2.

class CircleList:
  class Node:
    def __init__(self,data,nex=None,prev=None):
      self.next = nex
      self.prev = prev
      self.data = data

  def __init__(self):
    self.current = CircleList.Node(0)
    self.current.next = self.current
    self.current.prev = self.current

  def insert(self,data):
    self.current = self.current.next.next
    new_node = CircleList.Node(data,nex=self.current,prev = self.current.prev)
    self.current.prev.next = new_node
    self.current.prev = new_node
    self.current = new_node

  def remove(self):
    self.current = self.current.prev.prev.prev.prev.prev.prev.prev
    
    self.current.next.prev = self.current.prev
    self.current.prev.next = self.current.next
   
    placeholder = self.current
    self.current = self.current.next
    
    return placeholder.data


with open("input.txt","r") as f:
  data = f.read().rstrip("/n").split()

no_players = int(data[0])
last_marble = int(data[6]) * 100

players = [0] * no_players

circle = CircleList()

for i in range(1,last_marble+1):
  if i % 23 == 0:
    players[i%no_players] = players[i%no_players] + i + circle.remove()
  else:
    circle.insert(i)

print(max(players))

