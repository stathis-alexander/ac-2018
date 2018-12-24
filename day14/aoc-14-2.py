#!/usr/bin/python
# This is a solution to Advent of Code, day 14 part 2.


#puzzle_input = "2018"
#puzzle_input ="59414"
puzzle_input = "540391"

string = "37"
elf1 = 0
elf2 = 1

while puzzle_input not in string[-10:]:
  string += str(int(string[elf1])+int(string[elf2]))

  elf1 = (elf1 + int(string[elf1])+1) % len(string)
  elf2 = (elf2 + int(string[elf2])+1) % len(string)

print(string.index(puzzle_input))

