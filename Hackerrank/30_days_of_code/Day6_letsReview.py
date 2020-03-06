#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 20:31:10 2020

@author: aims
"""
N = int(input())

for i in range(0, N):

    string = input()

    for j in range(0, len(string)):
        if j % 2 == 0:
            print(string[j], end='')

    print(" ", end='')

    for j in range(0, len(string)):
        if j % 2 != 0:
            print(string[j], end='')

    print("")