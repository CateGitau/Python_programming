#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 07:24:22 2020

@author: aims
"""

class Calculator():
    def __init__(self, n, p):
        self.p = p
        self.n = ne
    def power(self):
        if self.p < 0 or self.n < 0:
            raise Exception ("n and p should be non-negative")
        else:
            return self.p**self.n

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e) 