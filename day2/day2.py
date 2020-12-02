import numpy as np

# https://adventofcode.com/2015/day/2

file = open('input.txt', 'r')

lines = file.readlines() 

total_paper = 0
total_ribbon = 0
for line in lines:
    [l,w,h] = np.array((line[:-1].split('x')), dtype=np.int)
    print(l, w, h)
    
    area1 = l*w
    area2 = w*h
    area3 = h*l
    
    
    total_paper += area1*2 + area2*2 + area3*2 + min(area1, area2, area3)
    
    dimensions_sorted = sorted([l, w, h])
    
    
    total_ribbon += dimensions_sorted[0]*2 + dimensions_sorted[1]*2 + dimensions_sorted[0]*dimensions_sorted[1]*dimensions_sorted[2]

    
print("Result part 1: ", total_paper)
print("Result part 1: ", total_ribbon)