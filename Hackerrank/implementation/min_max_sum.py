#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:11:01 2020

@author: aims
"""

arr = [1,2,3,4,5]

def minMax(arr):
    sums = []
    for i in arr:
        sums.append(sum(arr) - i)
    
    print(min(sums), max(sums))
        
(minMax(arr))