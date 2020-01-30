#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 09:36:50 2020

@author: aims
"""

"""
Given a square matrix, calculate the absolute difference between the sums of
 its diagonals. 
"""

matrix = [[11,2,4],[4,5,6],[10,8,-12]]

print(matrix[1][1])
n = len(matrix)
def diag_sum(matrix):
    forward = 0
    backward = 0
    for i in range(len(matrix)):
        
        for j in range(len(matrix[i])):
            if i == j:
                forward += matrix[i][j]
            if (i == n - j - 1):
                backward += matrix[i][j]
                
    return abs(forward - backward)

print(diag_sum(matrix))
            
            
            
            