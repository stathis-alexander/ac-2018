#!/usr/bin/python
# This is a solution to Advent of Code, day 16 part 1.

import sys

if len(sys.argv) > 1:
  filename = sys.argv[1]
else:
  filename = "input.txt"

with open(filename,"r") as f:
  lines = [line.rstrip("\n") for line in f.readlines()]

##
## FUNCTIONS
##

def addr(registers, A,B,C):
  registers[C] = registers[A] + registers[B]

def addi(registers, A,B,C):
  registers[C] = registers[A] + B

def mulr(registers, A,B,C):
  registers[C] = registers[A] * registers[B]

def muli(registers, A,B,C):
  registers[C] = registers[A] * B

def banr(registers, A,B,C):
  registers[C] = registers[A] & registers[B]

def bani(registers, A,B,C):
  registers[C] = registers[A] & B

def borr(registers, A,B,C):
  registers[C] = registers[A] | registers[B]

def bori(registers, A,B,C):
  registers[C] = registers[A] | B

def setr(registers, A,B,C):
  registers[C] = registers[A]

def seti(registers, A,B,C):
  registers[C] = A 

def gtir(registers, A,B,C):
  registers[C] = int(A > registers[B])

def gtri(registers, A,B,C):
  registers[C] = int(registers[A] > B)

def gtrr(registers, A,B,C):
  registers[C] = int(registers[A] > registers[B])

def eqir(registers, A,B,C):
  registers[C] = int(A == registers[B])

def eqri(registers, A,B,C):
  registers[C] = int(registers[A] == B)

def eqrr(registers, A,B,C):
  registers[C] = int(registers[A] == registers[B])

opcodes = { 0:addr, 1:addi, 2:mulr, 3:muli, 4:banr, 5:bani, 6:borr, 7:bori, 8:setr, 9:seti, 10:gtir, 11:gtri, 12:gtrr, 13:eqir, 14:eqri, 15:eqrr }

outputs = [int("1111111111111111",2)]*16

begin_instructions = 0

for i in range(len(lines)):
  lineno = i*4
  beforeline = lines[lineno]
 
  if "Before" not in beforeline:
    begin_instructions = lineno
    break

  opcodeline = lines[lineno+1]
  afterline =lines[lineno+2]

  Bregisters = [int(x) for x in beforeline.lstrip("Before: [").rstrip("]").split(", ")]
  Aregisters = [int(x) for x in afterline.lstrip("After: [").rstrip("]").split(", ")]
  OPCODE = [int(x) for x in opcodeline.split()]
 
  truthvalues = ""
  for j in range(16):
    registers = list(Bregisters)
    opcodes[j](registers, OPCODE[1],OPCODE[2],OPCODE[3])
    if registers == Aregisters:
      truthvalues += "1"
    else:
      truthvalues += "0"
  outputs[OPCODE[0]] &= int(truthvalues,2)


checked = []
function_table = {}
while any([list(bin(x).lstrip("0b").zfill(16)).count("1") > 1 for x in outputs]):
  for j in range(len(outputs)):
    if j in checked:
      continue
    bitstring = bin(outputs[j]).lstrip("0b").zfill(16)
    if list(bitstring).count("1") == 1:
      checked.append(j)
      for k in range(len(outputs)):
        if k != j:
          outputs[k] = (outputs[k] ^ outputs[j]) & outputs[k]  
      place_string = bitstring.index("1")
      function_table[j] = opcodes[place_string]
print("Opcode : Functions ")
for key in function_table:
  print(key,":",function_table[key])

while not lines[begin_instructions]:
  begin_instructions += 1

registers = [0,0,0,0]
for i in range(begin_instructions,len(lines)):
  nums = [int(x) for x in lines[i].split()]
  function_table[nums[0]](registers, nums[1],nums[2],nums[3])

print(registers[0])
