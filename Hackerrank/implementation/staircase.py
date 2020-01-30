#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:36:42 2020

@author: aims
"""

"""
print a staircase that is right-aligned, composed of # symbols and spaces, and has a 
height and width of .
"""

def staircase(n):
    for i in (range(1, n+1)):
        #adding rjust makes it right sided
        print(str('#'* i).rjust(n))
        
staircase(6)