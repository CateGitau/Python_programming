#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 23:01:02 2020

@author: aims
"""

nums = [3,6,1,0]

def largest_num(nums):
    large = max(nums)
    for i in range(len(nums)):
        if nums[i]*2 == large:
            return nums.index(large)
        else:
            return -1
            
        

print(largest_num(nums))
    