#!/bin/python3

import math
import os
import random
import re
import sys

def marcsCakewalk(calorie):
    # Sort the calories
    a = calorie
    a.sort(reverse=True)

    miles = 0
    count = 0

    # The larger the calorie, the smaller
    # the exponential should be in order to
    # compute the minimum walk
    for i in range(len(a)):
        miles += a[i] * (2 ** count)
        count += 1

    return miles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')
    fptr.close()
