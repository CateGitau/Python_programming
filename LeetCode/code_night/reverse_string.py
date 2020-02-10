#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 03:58:29 2020

@author: aims
"""

text = ["h","e","l","l","o"]

i = 0
j = len(text)- 1

while i<j:
    text[i], text[j] = text[j], text[i]
    i+=1
    j-=1
    
print(text)