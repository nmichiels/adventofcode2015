import numpy as np

# https://adventofcode.com/2015/day/1

file = open('input.txt', 'r')


data = file.readline()

floor = 0
firstBasement = 0
for i, c in enumerate(data):
    if c == '(':
        floor += 1
    if c == ')':
        floor -= 1
        
    if firstBasement == 0 and floor == -1:
        firstBasement = i+1
        
        
        
print("Solution part 1:", floor)
print("Solution part 2:", firstBasement)