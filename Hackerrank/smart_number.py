#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 07:54:45 2020

@author: aims
"""

"""
A number is called a smart number if it has an odd number of factors. 
Given some numbers, find whether they are smart numbers or not.

Debug the given function is_smart_number to correctly check if a given number 
is a smart number.

Note: You can modify only one line in the given code and you cannot add or 
remove any new lines.
"""
import math

num = 169

def is_smart_number(num):
    val = int(math.sqrt(num))
    #fact: perfect squares have odd factors
    if num / (val*val) == 1:
        return True
    return False
    
    #num_fact = 0
    #for i in range(1, num+1):
    #    if num % i == 0:
    #        num_fact += 1
    #if num_fact % 2 == 0:
    #    print ('NO')
    #else:
    #    print ('YES')
        

print(is_smart_number(num))