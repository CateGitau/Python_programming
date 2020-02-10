#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 00:22:10 2020

@author: aims
"""

nums = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]


def diagonal_traverse(nums):
    for i in range(len(nums)):
        for j in nums[i]:
            print(nums[i], nums[-1])

print(diagonal_traverse(nums))
    