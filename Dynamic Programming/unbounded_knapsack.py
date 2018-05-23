#!/bin/python3

import math
import os
import random
import re
import sys

def unboundedKnapsack(k, arr):
    # Essentially the coin change problem
    # with a slight difference to the return value
    mem = [0] * (k+1)
    mem[0] = 1

    arr = sorted(list(set(arr)))

    for val in arr:
        for i in range(val, k+1):
            mem[i] += mem[i-val]

    # Find the largest sum <= k that has a solution
    for i in range(k, 0, -1):
        if mem[i] > 0:
            return i

    # No solutions for any sum <= k
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for i in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()
