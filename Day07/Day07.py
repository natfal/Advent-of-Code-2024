#!/usr/bin/env python
import sys

def main():

    numbers = [];
    target = 0;
    currentLineResult = False;
    result = 0;

    for line in sys.stdin:
        s = line.split(" ")
        target = int(s[0].replace(":",""))
        numbers = [int(s) for s in s[1:]]
        
        currentLineResult = makeTargetP2(target, numbers, 1, numbers[0])

        if currentLineResult:
            result += target

        numbers.clear()

    print(result)


def makeTargetP1(target, numbers, currIndex, totalSoFar):
    if currIndex >= len(numbers):
        return target == totalSoFar

    add = makeTargetP1(target, numbers, currIndex + 1, totalSoFar + numbers[currIndex])
    multiply = makeTargetP1(target, numbers, currIndex + 1, totalSoFar * numbers[currIndex])

    return add or multiply

def makeTargetP2(target, numbers, currIndex, totalSoFar):
    if currIndex >= len(numbers):
        return target == totalSoFar

    add = makeTargetP2(target, numbers, currIndex + 1, totalSoFar + numbers[currIndex])
    multiply = makeTargetP2(target, numbers, currIndex + 1, totalSoFar * numbers[currIndex])
    concatenate = makeTargetP2(target, numbers, currIndex + 1, int(str(totalSoFar) + "" + str(numbers[currIndex])))

    return add or multiply or concatenate

if __name__ == "__main__":
    main()










