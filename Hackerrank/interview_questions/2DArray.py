#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 08:42:26 2020

@author: aims
"""


arr = [[1,1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

def hourglassSum(arr):
    all_hourglass = []
    for i in range(0, 4):
        for j in range(0, 4):
            hourglasses = []
            hourglasses+= arr[i][j:j+3]
            hourglasses.append(arr[i+1][j+1])
            hourglasses+= arr[i+2][j:j+3]
            
            all_hourglass.append(hourglasses)
            
    sum_hourglasses = []
    for item in all_hourglass:
        sum_hourglasses.append(sum(item))
    return(max(sum_hourglasses))
    
print(hourglassSum(arr))