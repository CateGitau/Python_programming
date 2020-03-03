#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:26:17 2020

@author: aims
"""

arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],
     [0,0,1,2,4,0]]

def hourglass(arr):
    all_hourglasses = []
    for i in range(0, 4):
        for j in range(0, 4):
            hourglasses = []
            hourglasses += arr[i][j:j+3]
            hourglasses.append(arr[i+1][j+1])
            hourglasses += arr[i+2][j:j+3]
            
            all_hourglasses.append(hourglasses)
    sum_h = []        
    for item in all_hourglasses:
        sum_h.append(sum(item))
    
    return max(sum_h)


print(hourglass(arr))
        