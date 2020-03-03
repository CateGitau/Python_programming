#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:31:48 2020

@author: aims
"""

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    lastNumber = 0
    seqList=[];
    for i in range(n):
        seqList.append([])
    res = [];
    for k, x, y in queries:
        index = (x^lastNumber)%n
        if k==1:
            seqList[index].append(y)
            #print(seqList)
        else:
            size = len(seqList[index])
            #print(seqList)
            #print(size)
            lastNumber = seqList[index][y%size]
            #print(lastNumber)
            res.append(lastNumber)
            
    return res 

    
    