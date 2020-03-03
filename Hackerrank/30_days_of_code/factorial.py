#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:45:58 2020

@author: aims
"""

n = int(input())

def factorial(n):
    if n<= 1:
        return n
    else:
        return n * factorial(n-1)
    
print(factorial(n))

