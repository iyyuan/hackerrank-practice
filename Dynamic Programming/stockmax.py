#!/bin/python3

import math
import os
import random
import re
import sys

def stockmax(prices):
    # We want to buy on all dates before the current maximum
    # Ex. given [1, 3, 1, 2]
    # - want to buy on day 1, sell on day 2
    # - want to buy on day 3, sell on day 4
    #
    # An equivalent solution is to reverse the prices and buy on
    # the prices less than the current max seen thus far
    #
    # The reverse is [2, 1, 3, 1]
    # We want to buy on all prices less than the max seen thus far
    # - want to buy at index 1 or prices[i] = 1, current_max = 2
    # - want to buy at index 3 or prices[i] = 1, current_max = 3

    profit = 0

    # Reverse all the prices
    prices.reverse()
    local_max = prices[0]

    # Buy when less than current_max
    for i in range(0, len(prices)):
        if prices[i] > local_max:
            local_max = prices[i]
        elif prices[i] < local_max:
            profit += local_max - prices[i]

    return profit

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
