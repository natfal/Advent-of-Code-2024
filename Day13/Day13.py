#!/usr/bin/env python
import sys
import numpy as np

tokens = (3, 1) # costs of (A, B)
excluded = []
included = []
A = []
B = []
prizeLoc = []
pushes = []
currIncluded = False

def main():

    result = 0
    
    buttonAText = "Button A:"
    buttonBText = "Button B:"
    prizeText = "Prize:"
    part1 = False

    for line in sys.stdin:
        if "Button A: " in line:
            A = [int(x) for x in line.replace(buttonAText, "").strip().replace("X+", "").replace("Y+", "").split(", ")]
            # print(A)
        elif "Button B:" in line:
            B = [int(x) for x in line.replace(buttonBText, "").strip().replace("X+", "").replace("Y+", "").split(", ")]
            # print(B)
        elif "Prize:" in line: 
            prizeLoc = [int(x) + (0 if part1 else 10000000000000) for x in line.replace(prizeText, "").strip().replace("X=", "").replace("Y=", "").split(", ")]
            # print(prizeLoc)
            pushes = getSimulEqValues(A, B, prizeLoc)
            result += calcMinTokens(A, B, prizeLoc, pushes)

    print(int(result))
 
def getSimulEqValues(A, B, expectedResults):
    coeffs = np.array([[A[0],B[0]],[A[1],B[1]]])
    expected = np.array(expectedResults)
    result = [round(x) for x in np.linalg.solve(coeffs, expected)]
    return result

def calcMinTokens(A, B, prizeLoc, pushes): # [numOfA, numOfB]
    result = 0
    if A[0]*pushes[0] + B[0]*pushes[1] == prizeLoc[0] and A[1]*pushes[0] + B[1]*pushes[1] == prizeLoc[1]:
        result = pushes[0] * tokens[0] + pushes[1] * tokens[1]
    return result
    
if __name__ == "__main__":
    main()