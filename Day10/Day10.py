#!/usr/bin/env python
import sys

trailsFound = []

def main():

    map = []
    part1 = True

    # create the map
    input = []
    for row, line in enumerate(sys.stdin):
        input = [int(x) for x in list(line.strip())]
        map.append([])
        for height in input:
            map[row].append(int(height))

    for r, row in enumerate(map):
        for c, col in enumerate(map):
            if map[r][c] == 0:
                trailsFound.append([])
                totalTrailsForPos(map, r, c, len(trailsFound) - 1, part1)
    result = sum([len(x) for x in trailsFound])
    print(result)
    
def inBounds(map, row, col):
    return row < len(map) and col < len(map[0]) and row >= 0 and col >= 0

def totalTrailsForPos(map, currRow, currCol, zeroID, part1Mode):
    if(not inBounds(map, currRow, currCol)):
        return 0
    if(map[currRow][currCol] == 9):
        if(part1Mode): # extra check for part1
            for l in trailsFound[zeroID]:
                if l[0] == currRow and l[1] == currCol:
                    return
        trailsFound[zeroID].append([currRow, currCol])
    upPos = [currRow - 1, currCol]
    rightPos = [currRow, currCol + 1]
    downPos = [currRow + 1, currCol]
    leftPos = [currRow, currCol - 1]
    # look up
    totalTrailsForPos(map, upPos[0], upPos[1], zeroID, part1Mode) if inBounds(map, upPos[0], upPos[1]) and map[currRow][currCol] + 1 == map[upPos[0]][upPos[1]] else 0
    # look right
    totalTrailsForPos(map, rightPos[0], rightPos[1], zeroID, part1Mode) if inBounds(map, rightPos[0], rightPos[1]) and map[currRow][currCol] + 1 == map[rightPos[0]][rightPos[1]] else 0 
    # look down
    totalTrailsForPos(map, downPos[0], downPos[1], zeroID, part1Mode) if inBounds(map, downPos[0], downPos[1]) and map[currRow][currCol] + 1 == map[downPos[0]][downPos[1]] else 0 
    # look left
    totalTrailsForPos(map, leftPos[0], leftPos[1], zeroID, part1Mode) if inBounds(map, leftPos[0], leftPos[1]) and map[currRow][currCol] + 1 == map[leftPos[0]][leftPos[1]] else 0

class Node:
    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount
        
    def __str__(self):
        return "(" + str(self.symbol) + "," + str(self.amount) + ")"

if __name__ == "__main__":
    main()