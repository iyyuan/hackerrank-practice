#!/bin/python3

import math
import os
import random
import re
import sys

def luckBalance(n, k, contests):
    print(contests)

    total = 0
    important = []

    for contest in contests:
        if contest[1] == 1:
            important.append(contest[0])
        else:
            total += contest[0]

    important.sort(reverse=True)

    # - Can afford to lose K important contests, so we
    #   want to lose the ones with the most luck
    # - Must win the rest; ideally the ones with the lowest luck
    #
    # Ex. given [8, 5, 2, 1]
    # lose = [8, 5, 2]
    # win = [1]
    lose = sum(important[:k])
    win = sum(important[k:])

    # Very confusing...
    # If you win, you lose luck BUT
    # If you lose, you gain luck
    total += lose - win
        
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(n, k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
