#!/usr/bin/python
# This is a solution to Advent of Code, day 14 part 1.

class CircleList:
  class Node:
    def __init__(self,data,nex=None,prev=None):
      self.next = nex
      self.prev = prev
      self.data = data

  def __init__(self):
    self.elf1 = CircleList.Node(3)
    self.elf2 = CircleList.Node(7,self.elf1,self.elf1)
    self.end = self.elf2

    self.elf1.prev = self.elf2
    self.elf1.next = self.elf2

    self.length = 2

  def combine_recipe(self):
    recipe = self.elf1.data + self.elf2.data
    number_str = str(recipe)
    for char in number_str:
      node = CircleList.Node(int(char),self.end.next,self.end)
      node.next.prev = node
      node.prev.next = node
      
      self.end = node
      self.length += 1

  def move_elves(self):
    recipe1 = self.elf1.data
    recipe2 = self.elf2.data

    for i in range(recipe1 + 1):
      self.elf1 = self.elf1.next
    for i in range(recipe2 + 1):
      self.elf2 = self.elf2.next

  def print_output(self,puzzle_input):
    start = self.end.next

    for i in range(puzzle_input):
      start = start.next

    for i in range(10):
      print(start.data,end="")
      start = start.next
    print()

#puzzle_input = 2018
puzzle_input = 540391

circle = CircleList()

while circle.length < puzzle_input + 10:
  circle.combine_recipe()
  circle.move_elves()

circle.print_output(puzzle_input)
