#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:58:00 2020

@author: aims

How many numbers are smaller than the current number

Given the array nums, 
for each nums[i] find out how many numbers in the array
are smaller than it. That is, for each nums[i] you have
count the number of valid j's such that j != i and 
nums[j] < nums[i].
"""

nums = [8,1,2,2,3]

count = []

ranks = {}
r = 0

for n in sorted(nums):
    if n not in ranks:
        ranks[n] = r
        
    r+= 1
    
for n in nums:
    count.append(ranks[n])

print(count)