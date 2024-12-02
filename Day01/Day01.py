#!/usr/bin/env python
import sys

# parse input
l, r, result = [], [], 0
part1mode = False

for line in sys.stdin:
    s = line.split()
    l.append(int(s[0]))
    r.append(int(s[1]))

if(part1mode):
    # part 1
    l.sort()
    r.sort()

    for il, ir in zip(l, r):
        result += abs(il - ir)

else:
# part 2
    lookup = {}

    for i in r:
        lookup.update({i: lookup[i] + 1 if i in lookup else 1})
    
    for i in l:
        result += i * lookup[i] if i in lookup else 0
        
print(result)










