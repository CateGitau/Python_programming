#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:07:41 2020

@author: aims
"""

scores = [17,45,41,60,17,41,76,43,51,40,89,92,34,6,64,7,37,81,32,50]

def breakingRecords(scores):
    high = []
    high.append(scores[0])
    low = []
    low.append(scores[0])
    
    count_max = 0
    count_min = 0
    
    for i, j in zip(scores[1:], high):
        if i < j:
            high.append(j)
        else:
            high.append(i)
            count_max += 1
            
    for i, k in zip(scores[1:], low):
        if i < k:
            low.append(i)
            count_min += 1
        elif i == k:
            low.append(i)
        else:
            low.append(k)
    print(high)
    print(low)        
    return(count_max, count_min)
    
print(breakingRecords(scores))