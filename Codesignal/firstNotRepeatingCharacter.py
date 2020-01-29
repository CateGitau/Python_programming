#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:42:50 2020

@author: aims
"""
s = "abaccabadd"

def firstNotRepeatingCharacter(s):
    char_order = []
    ctr = {}
    for c in s:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1 
            char_order.append(c)
    for c in char_order:
        if ctr[c] == 1:
            return c
    return '_'
      

print(firstNotRepeatingCharacter(s))
            
        
