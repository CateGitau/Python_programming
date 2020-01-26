#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:32:21 2020

@author: aims
"""

"""
You are in charge of the cake for your niece's birthday and have decided the
 cake will have one candle for each year of her total age. When she blows out 
 the candles, she’ll only be able to blow out the tallest ones. Your task is
 to find out how many candles she can successfully blow out.

For example, if your niece is turning 4
years old, and the cake will have candles of height 4,4,1,3 , she will be able 
to blow out 2 candles successfully, since the tallest candles are of height 4
and  there are 2 such candles. 

"""

arr = [3,2,1,3]

def birthdayCakeCandles(arr):
    candles = 0
    for i in range(len(arr)):
        maxim = max(arr)
        if arr[i] == maxim:
            candles += 1
    return candles
        
        
print(birthdayCakeCandles(arr))