#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 08:22:07 2020

@author: aims
"""

"""
You are given two-digit integer n. Returen sum of its digits
"""

n = 29

def AddTwoDigits(n):
    d1 = n % 10
    d2 = (n - d1)/10
    return d1+d2

print(AddTwoDigits(n))