#!/bin/python3

import math
import os
import random
import re
import sys

def candies(n, arr):
    candies = [1]

    # Check left to right
    for i in range(1, n):
        # Child to the right has a greater score,
        # and thus has one more candy than the child to the left
        if arr[i] > arr[i-1]:
            candies.append(candies[i-1] + 1)

        # Child to the right has a less than or equal score,
        # and thus can be given 1 candy
        else:
            candies.append(1)

    # Check right to left
    # This is to ensure than in a sequence such as [3, 2, 1]
    # the rightmost child has more candies than everyone else
    for i in range(n-1, 0, -1):
        # Child to the right has a lower score,
        # and thus the child to the left must have either
        # the maximum of what they are assigned in the first pass
        # or the number of candies the child to the right has + 1
        if arr[i-1] > arr[i]:
            candies[i-1] = max(candies[i-1], candies[i] + 1);

    return sum(candies)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
