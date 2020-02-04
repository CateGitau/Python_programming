#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:54:52 2020

@author: aims
"""

n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))