#!/usr/bin/env python
import sys

splits = {} # key for caching how many splits a () has

def main():
    
    part1 = True
    total = 0

    # create the map
    stones = []

    for line in sys.stdin:
        stones = [int(x) for x in line.strip().split(" ")]
    print(stones)

    total = len(stones)
    for x in stones:
        total += applyRules(x, 25 if part1 else 75)

    print(total)

# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
# The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
def applyRules(item, iterations):
    # no more iterations for this item
    if iterations == 0:
        return 0
    
    # check if in splits dict
    current = (item, iterations)
    if current in splits.keys():
        return splits.get(current)
    
    digits = int(len(str(item)))
    newIterations = iterations - 1
    result = 0
    # case 1
    if item == 0:
        result = applyRules(1, newIterations)
    # case 2
    elif digits % 2 == 0:
        result = 1 + applyRules(int(str(item)[int(digits/2):]), newIterations) + applyRules(int(str(item)[:int(digits/2)]), newIterations)
    # case 3
    else:
        result = applyRules(item * 2024, newIterations)
    
    # add to dict
    splits.update({current: result})
    return result
    
if __name__ == "__main__":
    main()