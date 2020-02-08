#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 22:41:43 2020

@author: aims
"""

nums = [1, 7, 3, 6, 5, 6]

def find_pivot(nums):
    for i in range(len(nums)):
        s1 = sum(nums[:i])
        s2 = sum(nums[i+1:])
        
        if s1 == s2:
            return (i)
        
    return -1

print(find_pivot(nums))
            
    