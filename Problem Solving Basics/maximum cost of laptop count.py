#!/bin/python3

import math
import os
import random
import re
import sys

def maxCost(cost, labels, dailyCount):
    max_cost = 0
    cur_count = 0
    current_cost = 0
    for c, l in zip(cost, labels):
        current_cost += c
        if l == "illegal":
            continue
        cur_count += 1
        if cur_count == dailyCount:
            max_cost = max(max_cost, current_cost)
            cur_count = 0
            current_cost = 0
    return max_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    cost_count = int(input().strip())

    cost = []

    for _ in range(cost_count):
        cost_item = int(input().strip())
        cost.append(cost_item)

    labels_count = int(input().strip())

    labels = []

    for _ in range(labels_count):
        labels_item = input()
        labels.append(labels_item)

    dailyCount = int(input().strip())

    result = maxCost(cost, labels, dailyCount)

    fptr.write(str(result) + '\n')

    fptr.close()