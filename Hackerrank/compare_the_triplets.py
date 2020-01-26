#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:58:42 2020

@author: aims
"""

a = (5,6,7)
b = (3, 6, 10)

def compareTriplets(a, b):
    
    alice = 0
    bob = 0
    for i,j in zip(a,b):
        if i > j:
            alice += 1
        elif j > i:
            bob += 1
        else:
            alice += 0
            bob += 0
            
    return alice, bob
        
        
        
print(compareTriplets(a,b))