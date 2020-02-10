#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 03:16:43 2020

@author: aims
"""
haystack = "hello"
needle = "ll"

def strStr(haystack: str, needle: str) -> int:
        stack = []
        for i, j in enumerate(haystack):
            for k, t in enumerate(needle):
                if j!= t:
                    i = i+1
                else:
                    stack.append(t)
                    
        print(stack)
        if stack == needle:
            return(i)
                        
print(strStr(haystack, needle))