#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(n, arr):
    # Sort the array
    a = arr
    a.sort()
    # Initially set the min difference to be +inf
    min_diff = math.inf

    # Compare difference of two consecutive numbers
    for i in range(0, n-1):
        if abs(a[i] - a[i+1]) < min_diff:
            min_diff = abs(a[i] - a[i+1])

    return min_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(n, arr)

    fptr.write(str(result) + '\n')
    fptr.close()
