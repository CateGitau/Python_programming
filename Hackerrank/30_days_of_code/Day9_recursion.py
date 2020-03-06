#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 07:56:40 2020

@author: aims
"""

# Complete the factorial function below.
def factorial(n):
    if n <=1:
        return n
        
    else:
        return n * factorial(n-1)