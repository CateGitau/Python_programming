#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:13:18 2020

@author: aims
"""

s, t = [2, 3]
a, b = [1,5]
m, n = [1,1]
apples = [-2]
oranges = [1]

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_dist = []
    orange_dist = []
    count_a = 0
    count_o = 0
    for i in apples:
        apple_dist.append(i + a)
    for i in oranges:
        orange_dist.append(i + b)
        print(orange_dist)
    
    for i in apple_dist:
        if i >= s and i<= t:
            count_a += 1
    print(count_a)
    for i in orange_dist:
        if i >= s and i <= t:
            count_o += 1
    print(count_o)
            
    #print(count_o, count_a)
    
   
    
    
countApplesAndOranges(s, t, a, b, apples, oranges)     
    
    
