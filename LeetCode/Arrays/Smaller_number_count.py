#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:58:00 2020

@author: aims
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
    print(ranks[n])