#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 13:44:40 2020

@author: aims
"""

a = "1 2 3 4"

# Complete the reverseArray function below.
def reverseArray(a):
    arr = []
    for i in reversed(a):
        arr.append(i)
    return arr