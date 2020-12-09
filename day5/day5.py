import re

# https://adventofcode.com/2015/day/5


def match_sentence_part2(sentence):
    if not re.match("[a-z]{2}\2",sentence):
        return True
    
    
def match_sentence(sentence):

    if not re.match(".*[aeiou].*[aeiou].*[aeiou].*",sentence):
        return False

    prev = sentence[0]
    found = False
    for i in range(1,len(sentence)):
        if sentence[i] == prev:
            found = True
            break
        prev = sentence[i]
            
    if not found:
        return False
        
    if re.match(".*ab.*",sentence):
        return False
        
    if re.match(".*cd.*",sentence):
        return False
    
    if re.match(".*pq.*",sentence):
        return False
        
        
    if re.match(".*xy.*",sentence):
        return False
        
        
    return True
            
            
    
    
    
  
file = open('input.txt', 'r')
lines = file.readlines()
num_nice = 0
for line in lines:
    if match_sentence(line):
        num_nice += 1

print("result part 1: ", num_nice)

print(match_sentence_part2('cd'))

