#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 07:16:38 2020

@author: aims
"""

arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],
     [0,0,1,2,4,0]]

my_hourglasses = list()

for i in range(0,4):
    for j in range(0,4):
        hourglass = list()
        hourglass += arr[i][j:j+3]
        hourglass.append(arr[i+1][j+1])
        hourglass += arr[i+2][j:j+3]
        my_hourglasses.append(hourglass)
#print(my_hourglasses)

hourglasses_sums = []
for item in my_hourglasses:
    hourglasses_sums.append(sum(item))

#hourglasses_sums = [sum(item) for item in my_hourglasses]

print(max(hourglasses_sums))
