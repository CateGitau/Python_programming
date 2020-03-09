#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:45:50 2020

@author: aims
"""
class Calculator():
    def power(self, n, p):
        if p < 0 or n < 0:
            raise Exception ("n and p should be non-negative")
        else:
            return n**p

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
