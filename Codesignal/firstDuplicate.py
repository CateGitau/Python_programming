#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 19:02:34 2020

@author: aims
"""

a = [2,1,3,2,5,3,2]

#def firstDuplicate(a):

#    dict = {}
#    found = 0

#    for i in range(len(a)):
#        if a[i] in dict:
#            dict[a[i]] += 1
#        else:
#            dict[a[i]] = 1

#        if(dict[a[i]] == 2):
#            return a[i]

#    if not found:
#        return -1
    
#print(firstDuplicate(a))

def firstDuplicate(a):
    set_a = set()
    
    for i in a:
        if i not in set_a:
            set_a.add(i)
        else:
            return (i)
        
print(firstDuplicate(a))
    