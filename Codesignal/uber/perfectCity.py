#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 23:18:50 2020

@author: aims
"""

l = 20
fares = [0.3, 0.5, 0.7, 1, 1.3]

def fancyRide(l, fares):
    total_cost = []
    rides = ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]
    for i in fares:
        total_cost.append(i * l)
    print(total_cost)
    
    car = max(i for i in total_cost if i <= 20)
    
    for i, j in zip(total_cost, rides):
        if i == car:
            return j
        
    #print(total_cost)
        
print(fancyRide(l, fares))
            
            
    
        
    
