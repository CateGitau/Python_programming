#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:25:58 2020

@author: aims
"""

a =  [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

def rotateImage(a):
    arr = []
    for i in range(len(a)):
        temp = []
        arr.append(temp)
        for j in range(len(a[i])):
            temp.append(a[(len(a) - 1) - j][i])
    print(arr)
    
    
            
    #print(a)
    
    
rotateImage(a)
            
            
            