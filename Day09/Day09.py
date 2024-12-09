#!/usr/bin/env python
import sys

def main():

    map = [] # list of nodes
    part1 = False

    # create the map
    id = 0
    tempNode = Node(".", 0)
    input = []

    for line in sys.stdin:
        input = list(line)
        for idx, s in enumerate(input):
            tempNode.amount = int(s)
            tempNode.symbol = "." if idx % 2 != 0 else id
            if idx % 2 != 0:
                id += 1
            map.append(Node(tempNode.symbol, tempNode.amount))

    if part1:
        currentIndex = len(map) - 1
        foundSlot = False
        while currentIndex > 0:
            foundSlot = False
            if map[currentIndex].symbol == ".":
                currentIndex -= 1
                continue
            for idx, node in enumerate(map[:currentIndex]):
                if node.symbol == "." and node.amount > 0:
                    map[currentIndex].amount -= 1
                    node.amount -= 1
                    map.insert(idx, Node(map[currentIndex].symbol, 1))
                    foundSlot = True
                    break
            if not foundSlot:
                currentIndex -= 1
            elif map[currentIndex + 1].amount > 0:
                currentIndex += 1
    else: # part2
        currentIndex = len(map) - 1
        foundSlot = False
        while currentIndex > 0:
            foundSlot = False
            if map[currentIndex].symbol == ".":
                currentIndex -= 1
                continue
            for idx, node in enumerate(map[:currentIndex]):
                tempAmount = map[currentIndex].amount
                if node.symbol == "." and node.amount >= tempAmount:
                    node.amount -= tempAmount
                    map.insert(idx, Node(map[currentIndex].symbol, tempAmount))
                    map[currentIndex + 1].symbol = "."
                    foundSlot = True
                    break
            if not foundSlot:
                currentIndex -= 1
            elif map[currentIndex + 1].amount > 0:
                currentIndex += 1
    
    for node in map:
        print(node)
    
    print(calcCheckSum(generateMap(map)))

def generateMap(list): # list of Nodes
    map = []
    for node in list:
        for i in range(node.amount):
            map.append(node.symbol)
    return map


def calcCheckSum(map):
    sum = 0
    idx = 0
    for idx, c in enumerate(map):
        if(c != "."):
            sum += int(c) * idx
    return sum

class Node:
    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount
        
    def __str__(self):
        return "(" + str(self.symbol) + "," + str(self.amount) + ")"

if __name__ == "__main__":
    main()
