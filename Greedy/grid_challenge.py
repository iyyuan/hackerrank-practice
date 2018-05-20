#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):

    # Sort each row
    for i in range(n):
        grid[i] = sorted(grid[i])

    # Ensure each character in (row/column) comes
    # before the character in (row+1,column)
    # in the alphabet
    for row in range(n-1):
        for col in range(n):
            # If a character in the row above comes after
            # Return "NO"
            if grid[row][col] > grid[row+1][col]:
                return "NO"

    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    # Why is this line missing by default...?
    for i in range(t):
        n = int(input())
        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
