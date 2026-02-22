#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countSubarraysWithSumAndMaxAtMost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. LONG_INTEGER k
#  3. LONG_INTEGER M
#

def countSubarraysWithSumAndMaxAtMost(nums, k, M):
    sub_array=[]
    custom_array=[]
    n=len(nums)
    sum_custom=0
    i=0
    for i in range(n):
        greater=False
        for j in range(i,n):
            custom_array=nums[i:j+1]
            for element in custom_array:
                if element > M:
                    greater=True
                    break
            if greater:
                break
            sum_custom=sum(custom_array)
            if sum_custom==k:
                sub_array.append(custom_array.copy())
    return len(sub_array)
    # Write your code here

if __name__ == '__main__':
    # nums_count = int(input().strip())

    # nums = []

    # for _ in range(nums_count):
    #     nums_item = int(input().strip())
    #     nums.append(nums_item)

    k = int(input().strip())

    M = int(input().strip())

    result = countSubarraysWithSumAndMaxAtMost([1, 10, 1], k, M)
    print(result)