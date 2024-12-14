#!/usr/bin/env python
import sys

columns = 101
rows = 103
midRow = int(rows / 2)
midColumn = int(columns / 2)
countInQuadrants = [0, 0, 0, 0] # Q 1, 2, 3, 4
positions = []
velocities = []
part1 = False
maxIterations = rows * columns # positions will all reset after this many runs bc of modulo
grid = []

def main():

    for line in sys.stdin:
        temp = line.strip().split(" ")

        p = [int(x) for x in temp[0].replace("p=", "").split(",")] # second number in is the row
        tempNum = p[0]
        p[0] = p[1]
        p[1] = tempNum

        v = [int(x) for x in temp[1].replace("v=", "").split(",")] # second number in is the row
        tempNum = v[0]
        v[0] = v[1]
        v[1] = tempNum

        positions.append(p)
        velocities.append(v)

    if(part1):
        for p, v in zip(positions, velocities):
            move(p, v, 100)

        print(positions)

        for x in positions:
            addToQuadrant(x)

        print(calcSafetyFactor())
    else:
        for idx in range(rows):
            grid.append([])
            for idx2 in range(columns):
                grid[idx].append(".")

        for x in range(maxIterations):
            for p, v in zip(positions, velocities):
                move(p, v, 1)
            updateGrid()
            for r in grid:
                if "XXXXXXXXX" in "".join(r):
                    print("ITERATION: " + str(x + 1))
                    printTree()
            

def move(pos, vel, times):
    pos[0] = (pos[0] + vel[0] * times) % rows
    pos[1] = (pos[1] + vel[1] * times) % columns

def addToQuadrant(p):
    rowCond = p[0] < midRow
    colCond = p[1] < midColumn

    if p[0] == midRow or p[1] == midColumn:
        return

    quadrant = (1 if colCond else 2) if rowCond else (3 if colCond else 4)
    countInQuadrants[quadrant - 1] += 1

def calcSafetyFactor():
    result = 1
    for x in countInQuadrants:
        result *= x
    return result

def printTree():
    for x in grid:
        for y in x:
            print(y, end="")
        print()

def updateGrid():
    clearGrid()
    for x in positions:
        grid[x[0]][x[1]] = "X"

def clearGrid():
    for idx in range(rows):
            for idx2 in range(columns):
                grid[idx][idx2] = "."


if __name__ == "__main__":
    main()