#!/bin/python3

import math
import os
import random
import re
import sys

def fibonacciModified(t1, t2, n):
    # Use a dict for memoization
    mem = {}
    mem[1] = t1
    mem[2] = t2

    for i in range(3,n+1):
        mem[i] = mem[i-2] + mem[i-1]**2
    return mem[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t1T2n = input().split()

    t1 = int(t1T2n[0])
    t2 = int(t1T2n[1])
    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)
    fptr.write(str(result) + '\n')
    fptr.close()
