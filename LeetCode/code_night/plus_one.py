#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 23:25:18 2020

@author: aims
"""
nums = [1,2,3,9]
def plus_one(nums):
    if len(nums) == 0:
        return [1]
    
    sol = []
    carry = 1
    
    for i in range(len(nums)-1, -1, -1):
        s = carry + nums[i]
        if s >= 10:
            carry = 1
            sol.append(s%10)
        else:
            carry = 0
            sol.append(s)
            
    if carry == 1:
        sol.append(1)
        
    return sol[::-1]

print(plus_one(nums))