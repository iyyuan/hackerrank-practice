#!/bin/python3

import math
import os
import random
import re
import sys

def getWays(n, c):
    mem = [0] * (n+1)
    mem[0] = 1

    for coin in c:
        for i in range(coin, n+1):
            mem[i] += mem[i-coin]

    return mem[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))

    fptr.write(str(getWays(n, c)))

    fptr.close()
