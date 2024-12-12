#!/usr/bin/env python
import sys

up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)

topRight = (-1, 1)
bottomRight = (1, 1)
bottomLeft = (1, -1)
topLeft = (-1, -1)

field = []
visited = []
regionValues = [] # [area, perimeter]
part1 = False

def main():
    
    total = 0
    regionNumber = 0

    for line in sys.stdin:
        field.append(list(line.strip()))
        visited.append([False for i in range(len(line.strip()))])

    print(field)

    for r, f in enumerate(field):
        for c, x in enumerate(f):
            if(visited[r][c] == False):
                regionValues.append([0, 0])
                calcRegion(field[r][c], regionNumber, r, c)
                regionNumber += 1
                        
    for x in regionValues:
        total += x[0] * x[1]

    print(regionValues)

    print(total)

def calcRegion(crop, regionNumber, r, c):
    regionValues[regionNumber][0] += 1 # increase the area
    visited[r][c] = True

    uP = (r + up[0], c + up[1])
    rP = (r + right[0], c + right[1])
    dP = (r + down[0], c + down[1])
    lP = (r + left[0], c + left[1])

    tRP = (r + topRight[0], c + topRight[1])
    bRP = (r + bottomRight[0], c + bottomRight[1])
    bLP = (r + bottomLeft[0], c + bottomLeft[1])
    tLP = (r + topLeft[0], c + topLeft[1])

    positions = [uP, rP, dP, lP]
    diagonals = [tRP, bRP, bLP, tLP]
    sameCropPositions = [1 if inBounds(x) and field[x[0]][x[1]] == crop else 0 for x in positions]
    sameCropDiagonals = [1 if inBounds(x) and field[x[0]][x[1]] == crop else 0 for x in diagonals]
    countPerimeter = 4 - sum(sameCropPositions) # only matters if it's part 1
    countCorners = 0 # only matters if it's part 2

    for x in zip(positions, sameCropPositions):
        if(x[1] and not visited[x[0][0]][x[0][1]]):
            calcRegion(crop, regionNumber, x[0][0], x[0][1])

    if part1:
        regionValues[regionNumber][1] += countPerimeter
    else:
        # part2 calc - get the number of corners
        # a cell has a corner if the right & left are the same type, but not the diagonal (do the same for each "side")
        for idx, i in enumerate(sameCropPositions):
            nextPos = sameCropPositions[(idx + 1) % len(sameCropPositions)]
            if (i + nextPos) == 0 or ((i + nextPos) == 2 and sameCropDiagonals[idx] == 0):
                print(r, c, "hi:", i + nextPos)
                countCorners += 1
        regionValues[regionNumber][1] += countCorners
    
def inBounds(t): # pass a tuple as position
    rows = len(field)
    columns = len(field[0])
    return t[0] >= 0 and t[0] < rows and t[1] >= 0 and t[1] < columns
    
if __name__ == "__main__":
    main()