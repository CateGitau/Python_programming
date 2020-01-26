#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:14:25 2020

@author: aims
"""

"""
Given an array of integers, calculate the fractions of its elements that are 
positive, negative, and are zeros. Print the decimal value of each fraction on 
a new line.
"""

arr = [1,1,0,-1,-1]

def plus_minus(arr):
    n = len(arr)
    pos = []
    neg = []
    zer = []
    
    for i in range(len(arr)):
        if arr[i] > 0:
            pos.append(arr[i])
        elif arr[i] < 0:
            neg.append(arr[i])
        else:
            zer.append(arr[i])   
    
    print(format(len(pos)/n, '.6f'))
    print(format(len(neg)/n, '.6f'))
    print(format(len(zer)/n, '.6f'))
    

