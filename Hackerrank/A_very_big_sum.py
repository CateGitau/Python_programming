#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 09:17:53 2020

@author: aims
"""

"""
return the sum of all array elements.
"""

arr = (1000000001,1000000002,1000000003,1000000004,1000000005)

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    big_sum = 0
    for i in ar:
        big_sum += i
    return big_sum

print(aVeryBigSum(arr))
    