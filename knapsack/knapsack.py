#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  for i in range(len(items)):
    items[i].eff = items[i].value / items[i].size
    
  items.sort(key=lambda x: x.eff, reverse=True)

  sack = []
  value = 0
  for item in items:
    capacity -= item.size
    value += item.value
    if capacity <= 1:
      return {Value: value, Chosen: sack}
    sack.append(item.index)



if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')