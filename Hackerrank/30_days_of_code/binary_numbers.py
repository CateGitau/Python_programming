#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:51:13 2020

@author: aims
"""

n = 439

def binary(n):
    max_count = 0
    one_count = 0
    bn = bin(n).replace("0b", "")
    for i in bn:
        if i == '1':
            one_count += 1
        else:
            max_count = max(max_count, one_count)
            one_count = 0
      
    return max(max_count, one_count)

print(binary(439))
    

    
