import re
import numpy as np

# https://adventofcode.com/2015/day/6

    
  
file = open('input.txt', 'r')
lines = file.readlines()

grid = np.zeros((1000,1000), dtype=np.uint8)
for line in lines:
    coordinates = np.asarray(re.findall(r'\d+', line), np.int)

    if re.search(r'on', line):
        print("Turn on")
        grid[coordinates[0]:coordinates[2]+1,coordinates[1]:coordinates[3]+1] = 1
    if re.search(r'off', line):
        print("Turn off")
        grid[coordinates[0]:coordinates[2]+1,coordinates[1]:coordinates[3]+1] = 0
        
    if re.search(r'toggle', line):
        print("Toggle")
        grid[coordinates[0]:coordinates[2]+1,coordinates[1]:coordinates[3]+1] = 1 - grid[coordinates[0]:coordinates[2]+1,coordinates[1]:coordinates[3]+1]
        

print("Result part 1: ", np.count_nonzero(grid))


grid = np.zeros((1000,1000), dtype=np.int8)
for line in lines:
    coordinates = np.asarray(re.findall(r'\d+', line), np.int)

    if re.search(r'on', line):
        print("Turn on")
        grid[coordinates[0]:coordinates[2]+1,coordinates[1]:coordinates[3]+1] += 1
    if re.search(r'off', line):
        print("Turn off")
        grid[coordinates[0]:coordinates[2]+1,coordinates[1]:coordinates[3]+1] -= 1
        grid = np.maximum(grid, 0)
        
    if re.search(r'toggle', line):
        print("Toggle")
        grid[coordinates[0]:coordinates[2]+1,coordinates[1]:coordinates[3]+1] +=2
        
        
print("Result part 2: ", np.sum(grid))