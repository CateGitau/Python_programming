#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:47:48 2020

@author: aims
"""

nums = [1,2,3,4]

arr = []
for i in range(0,len(nums),2):
    print(range(nums[i]))
    for j in range(nums[i]):
        arr.append(nums[i+1])

print(arr)