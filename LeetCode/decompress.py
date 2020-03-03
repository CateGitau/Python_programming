#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:47:48 2020

@author: aims
"""

nums = [1,2,3,4]

totals = []
for i in range(0, len(nums), 2):
    counts = []
    times = nums[i]
    vals = str(nums[i+1])
    
    counts.append(int((vals * times)))
    
    totals+=(counts)
print(totals)
    