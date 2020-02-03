#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:28:13 2020

@author: aims
"""

ar = [1,3,2,6,1,2]
n = 6
k = 3

def divisibleSumPairs(ar):
    res = 0
    for i in range(0, n):
        for j in range(i+1, n):
            
            if (ar[i] + ar[j]) % k == 0:
                res+=1
    print(res)
                
        
        
print(divisibleSumPairs(ar))