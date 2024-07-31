# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    zero = len([x for x in arr if x == 0])
    neg = len([x for x in arr if x < 0])
    pos = len(arr) - (zero+neg)
    
    
   
    print(f"{pos/n:.6f}")
    print(f"{neg/n:.6f}")
    print(f"{zero/n:.6f}")
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


# https://www.hackerrank.com/interview/preparation-kits/one-week-preparation-kit/one-week-day-one/challenges

# question https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one