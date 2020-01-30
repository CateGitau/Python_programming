#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:51:12 2020

@author: aims
"""

ar = [10,20,20,10,10,30,50,10,20]
n = 9

def sockMerchant(n , ar):
    dic = {}
    pairs = 0
    for i in range(0, n):
        if ar[i] not in dic:
            dic[ar[i]] = 1
        else:
            dic[ar[i]] += 1
    
    for i in dic.values():
        pairs += (i//2)
    
    return pairs
    
print(sockMerchant(ar))
            
        
            
        