#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:34:12 2020

@author: aims
"""

input = 3

def condition(input):
    if input % 2 != 0:
        print('Weird')
    elif input % 2 == 0 and 2 <= input <= 5:
        print ('Not Weird')
    elif input % 2 == 0 and 6  <= input <= 20:
        print('Weird')
    else:
        print('Not Weird')
        

condition(input)
    