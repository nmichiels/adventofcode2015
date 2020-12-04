import hashlib 

# https://adventofcode.com/2015/day/4

input = 'bgvyzdsv'


number = 1
key = input + str(number)

while hashlib.md5(key.encode()).hexdigest()[0:5] != '00000':
    number+=1
    key = input + str(number)

print("Result part 1: ", number)



number = 1
key = input + str(number)

while hashlib.md5(key.encode()).hexdigest()[0:6] != '000000':
    number+=1
    key = input + str(number)
    
print("Result part 2: ", number)