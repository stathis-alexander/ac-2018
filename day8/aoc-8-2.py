#!/usr/bin/python
# This is a solution to Advent of Code, day 8 part 1.

with open("input.txt","r") as f:
  data = [int(x) for x in f.read().rstrip("/n").split()]

class Node:
  def __init__(self):
    self.metadata = []
    self.children = []
  def children(self):
    return self.children
  def metadata(self):
    return self.metadata

def build_children(data):
  no_of_children = data[0]
  no_of_meta = data[1]

  data = data[2:]

  #print(no_of_children,no_of_meta)
  
  parent = Node()

  if no_of_children == 0:
    meta_data = data[:no_of_meta]
    data = data[no_of_meta:]
    parent.metadata = meta_data
    #print(meta_data)
    return parent,data

  for i in range(no_of_children):  
    #print("child",i,"of",no_of_children,":",no_of_meta,data[:10])
    child,new_data = build_children(data)
    parent.children.append(child)
    data = new_data

  parent.metadata = data[:no_of_meta]
  data = data[no_of_meta:]

  return parent,data
    
root_node,data = build_children(data)

def sum_meta_data(root_node):
  meta_sum = sum(root_node.metadata)
  
  for child in root_node.children:
    meta_sum += sum_meta_data(child)
  return meta_sum

print(sum_meta_data(root_node))


