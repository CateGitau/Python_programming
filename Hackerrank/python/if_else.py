#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:10:19 2020

@author: aims
"""
n = int(input())

if n % 2 != 0:
    print('Weird')
elif n%2 == 0 and 2<= n<= 5:
    print('Not Weird')
elif n%2 == 0 and 6 <= n<= 20:
    print('Weird')
else:
    print('Not Weird')