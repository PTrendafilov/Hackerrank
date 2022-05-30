#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    vowels = ["a", "e", "i", "o", "u"]
    max_vowels = sum([c in vowels for c in s[0:k]])
    current = sum([c in vowels for c in s[0:k]])
    best_substring_index = 0
    for i in range(k, len(s)):
        current += s[i] in vowels
        current -= s[i - k] in vowels
        if current > max_vowels:
            max_vowels = current
            best_substring_index = i - k + 1
    if max_vowels > 0:
        return s[best_substring_index:(best_substring_index+k)]
    else:
        return "Not found!"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)

    fptr.write(result + '\n')

    fptr.close()