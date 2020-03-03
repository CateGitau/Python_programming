#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:47:51 2020

@author: aims
"""

def rotate(a, r):
    l = a[r:] + a[:r]
    return l


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    r = d % n

    print(*rotate(a,r)) 
