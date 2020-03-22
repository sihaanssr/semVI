
tokens = [[] for x in range(4)]

with open('object-code1.txt') as code:
    text = code.readlines()
    position = 0
    for line in text:
        tokens[position] = line.split('^')
        position+=1

print('The name of object code : {}'.format(tokens[0][1]))

for line in tokens[1:]:
    if line[0]=='E':
        break
    counter = int(line[1])
    for elements in line[3:]:
        print('{}\t{}'.format(counter,elements[0:2]))
        counter += 1
        print('{}\t{}'.format(counter,elements[2:4]))
        counter += 1
        print('{}\t{}'.format(counter,elements[4:]))
        counter += 1

"""
Object code:
H^SAMPLE^001000^0035
T^001000^0C^001003^071009
T^002000^03^111111
E^001000
The name of object code : SAMPLE
1000    00
1001    10
1002    03
1003    07
1004    10
1005    09
2000    11
2001    11
2002    11

The object code files are both test cases for this experiment.
"""