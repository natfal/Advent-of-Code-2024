#!/usr/bin/env python
import sys

test = False
distance = 7 if test else 71
part1 = False
simulationLimit = 12 if test else 1024 if part1 else 2900 # tweaked this until it was nearing the limit - could do a similar approach with binary search 

corrupted = []
toVisit = []
visited = []
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # U, R, D, L
pathLengths = []

def main():
    for line in sys.stdin:
        temp = line.strip().split(",")
        corrupted.append((int(temp[1]), int(temp[0])))

    initialisePathLengths()
    initialiseVisited()

    if(part1):
        print(traverseGrid())
    else:
        global simulationLimit
        while simulationLimit <= len(corrupted):
            print(simulationLimit)
            if (traverseGrid() == -1):
                result = corrupted[simulationLimit - 1]
                print(str(result[1]) + "," + str(result[0]))
                break     
            else:
                initialisePathLengths()
                initialiseVisited()
                simulationLimit += 1
            
def initialisePathLengths():
    pathLengths.clear()
    for x in range(distance):
        pathLengths.append([])
        for y in range(distance):
            pathLengths[x].append(0)

def initialiseVisited():
    visited.clear()
    toVisit.clear()
    for x in range(distance):
        visited.append([])
        for y in range(distance):
            visited[x].append(False)

def traverseGrid():
    toVisit.append((0,0))

    while(toVisit):
        pos = toVisit.pop(0)
        visited[pos[0]][pos[1]] = True

        global distance
        if pos[0] == distance - 1 and pos[1] == distance - 1:
            return pathLengths[pos[0]][pos[1]]
        
        tempLength = pathLengths[pos[0]][pos[1]]
        
        for i in range(4):
            newPos = (pos[0] + directions[i][0], pos[1] + directions[i][1]) # could change to pos + directions[i]

            if inGrid(newPos) and not isCorrupted(newPos) and not hasVisited(newPos):
                pathLengths[newPos[0]][newPos[1]] = tempLength + 1
                if not newPos in toVisit:
                    toVisit.append(newPos) 

    return -1

def inGrid(pos): # pass a tuple
    global distance
    return pos[0] >= 0 and pos[0] < distance and pos[1] >= 0 and pos[1] < distance

def hasVisited(pos):
    return visited[pos[0]][pos[1]]

def isCorrupted(pos):
    global corrupted
    return pos in corrupted[:simulationLimit]

if __name__ == "__main__":
    main()

