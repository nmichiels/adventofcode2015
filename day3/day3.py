import numpy as np

# https://adventofcode.com/2015/day/3

file = open('input.txt', 'r')

instructions = file.readline() 

# print(len(instructions))


def run(instructions, houses):

    row = 0
    col = 0
    houses[ hash(str(row)+','+str(col))] = 1
    
    for instruction in instructions:
        
        if instruction == '>':
            col += 1
            
        if instruction == '<':
            col -= 1
            
        if instruction == '^':
            row -= 1
            
        if instruction == 'v':
            row += 1
            
            
        # print((row,col), hash((row,col)))
        houses[ hash(str(row)+','+str(col))] = 1
        


# part 1
houses = {}
run(instructions, houses)
print("Number of houses:", len(houses))

# part 2
houses = {}
run(instructions[::2], houses) #even
run(instructions[1::2], houses) #odd
print("Number of houses with robot:", len(houses))