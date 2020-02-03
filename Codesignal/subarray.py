#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 08:31:33 2020

@author: aims
"""

"""
A subarry is a contiguous portion of an array. GIven an array of integers
numbers and an integer k, your task is to determine the number of distinct 
subarrays of numbers with at most k odd elements. Two subarrays are considered
distinct if their contents differ in at least one position.

"""

my_list = [3,2,3,4]
m = 1

def sub_lists1(my_list):
    subs = []
    for i in range(len(my_list)):
        n = i+1
        while n <= len(my_list):
            sub = my_list[i:n]
            subs.append(sub)
            n += 1

    return subs

print(sub_lists1(my_list))

def sub_lists2(my_list, m):
    count = 0
    
    for i in range(len(my_list)):
        odd = 0
        for j in range(i,len(my_list)):
            if (my_list[j]):
                odd += 1
            if odd == m:
                count += 1;
    return count

print(sub_lists2(my_list, m))

def sublists3(my_list):
    s = []
    j = 0
    
    for i in range(len(my_list)):
        
        while (j < len(my_list) and (my_list[j] not in s)):
            s.append(my_list[j])
            j +=1
    print(s)

#sublists3(my_list)