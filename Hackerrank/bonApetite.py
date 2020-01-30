#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:21:57 2020

@author: aims
"""

n, k = (4, 1)
charge = [3,10,2,9]
b = 12


def bonAppetit(bill, k, b):
    total = sum(bill)
    final = (total - bill[k])/2
        
    if final == b:
        print('Bon Appetit')
    else:
        print(int(b - final))


bonAppetite(n, k, charge, b)
        