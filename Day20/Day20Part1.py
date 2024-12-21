#!/usr/bin/env python
import sys

racetrack = []
part1 = True
winningPath = [] # no cheating, also includes startPos (remove 1 from length for time taken)
startPos = ()
endPos = ()
picoSecondsSaved = []

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # U, R, D, L

def main():
    for line in sys.stdin:
        racetrack.append(list(line.strip()))
    
    findStartingAndEndingPos()

    winningPath.append(startPos)
    currPos = startPos
    while(currPos != None):
        currPos = findWinningPath(currPos, endPos)
    winningPath.append(endPos)

    for idx, x in enumerate(winningPath):
        tryToCheat(x, idx, False)

    # print(picoSecondsSaved)
    result = sum(1 for x in picoSecondsSaved if x >= 100)
    print(result)

def addDirection(pos, direction):
    return (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
        
def findWinningPath(startingPos, endingPos):
    for idx in range(4):
        newPos = addDirection(startingPos, idx)
        if not newPos in winningPath and racetrack[newPos[0]][newPos[1]] == '.':
            winningPath.append(newPos)
            return newPos

def findStartingAndEndingPos():
    global startPos, endPos
    for row, x in enumerate(racetrack):
        if 'S' in x:
            startPos = (row, x.index("S"))
        if 'E' in x:
            endPos = (row, x.index("E"))

def cheating(cheatLocation, secondsUsed, cheated): # add seconds saved to picoSecondsSaved
    for idx in range(4):
        newPos = addDirection(cheatLocation, idx)
        if inBounds(newPos):
            if (racetrack[newPos[0]][newPos[1]] == '.' or racetrack[newPos[0]][newPos[1]] == 'E'):
                # print(cheatLocation)
                # print(newPos)
                timeSaved = winningPath.index(newPos) - secondsUsed
                # if(timeSaved == 64):
                #     print("HERE:", cheatLocation, newPos)
                #     print("cheated:", cheated)
                picoSecondsSaved.append(timeSaved)
            #### USED WHEN ASSUMED COULD DO MORE THAN ONE
            # elif racetrack[newPos[0]][newPos[1]] == '#' and cheated == False: # for the two second cheat
            #     tryToCheat(cheatLocation, secondsUsed - 1, True)

def tryToCheat(pos, secondsUsed, cheated):
    for idx in range(4):
        newPos = addDirection(pos, idx)
        if inBounds(newPos) and racetrack[newPos[0]][newPos[1]] == '#':
            cheating(newPos, secondsUsed + 2, cheated)

def inBounds(pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(racetrack) and pos[1] < len(racetrack[0])

if __name__ == "__main__":
    main()