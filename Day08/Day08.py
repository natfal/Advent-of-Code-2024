#!/usr/bin/env python
import sys

def main():

    map = []
    symbolLocations = {} # key is char, value is list of Points
    antennaLocations = [] # list of points
    distance = Point(0, 0)
    newAntennaLocation = Point(0, 0)
    part1 = True

    for row, line in enumerate(sys.stdin):
        s = list(line.strip())
        map.append(s)
        for column, symbol in enumerate(line):
            if symbol == ".": 
                continue
            if symbol not in symbolLocations.keys():
                symbolLocations[symbol] = []
            symbolLocations[symbol].append(Point(row, column))

    if part1:
        for key in symbolLocations:
            values = symbolLocations.get(key)
            for v1 in values:
                for v2 in values:
                    if v1 == v2:
                        continue
                    distance = Point(v2.row - v1.row, v2.column - v1.column)
                    newAntennaLocation = Point(v2.row + distance.row, v2.column + distance.column)
                    if pointOnMap(map, newAntennaLocation) and not antennaExists(antennaLocations, newAntennaLocation): # and not symbolExists(map, newAntennaLocation)
                            antennaLocations.append(newAntennaLocation)
        print(len(antennaLocations))
    else: # part2
        check1 = True
        # check2 = True
        check3 = True
        for key in symbolLocations:
            values = symbolLocations.get(key)
            for v1 in values:
                for v2 in values:
                    if v1 == v2:
                        continue
                    distance = Point(v2.row - v1.row, v2.column - v1.column)
                    currentPoint = v1
                    
                    check1 = True
                    while check1:
                        newAntennaLocation = Point(currentPoint.row + distance.row, currentPoint.column + distance.column)
                        check1 = pointOnMap(map, newAntennaLocation)
                        if check1:
                            # check2 = not symbolExists(map, newAntennaLocation)
                            check3 = not antennaExists(antennaLocations, newAntennaLocation)
                            if check3: # if check2 and check3:
                                antennaLocations.append(newAntennaLocation)
                            currentPoint = newAntennaLocation
        # for i in range(12):
        #     for x in antennaLocations:
        #         if x.row == i:
        #             print(x)
        print(len(antennaLocations))

# Not required - antinodes can exist where antennas exist
# def symbolExists(map, point):
#     return map[point.row][point.column] != "."

def antennaExists(locations, point):
    for p in locations:
        if p == point:
            return True
    return False

def pointOnMap(map, point):
    rows = len(map)
    columns = len(map[0])
    return point.row < rows and point.column < columns and point.row >= 0 and point.column >= 0

class Point:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        
    def __str__(self):
        return "(" + str(self.row) + ", " + str(self.column) + ")"
    
    def __eq__(self, other):
        return self.row == other.row and self.column == other.column


if __name__ == "__main__":
    main()










