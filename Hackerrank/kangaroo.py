#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:50:50 2020

@author: aims
"""

x1, v1, x2, v2 = [21,6,47,3]

def kangaroo(x1, v1, x2, v2):
    
    #n = (x1 - x2)/(v2-v1)
    
    if x1 < x2 and v1 > v2:
        if (v2-v1)!= 0 and (x1 - x2) % (v2-v1) == 0:
            return 'YES'
        else:
            return 'NO'
        
    else:
        return 'NO'
    

print(kangaroo(x1, v1, x2, v2))       
    

#in one line of code

#def kangaroo(x1, v1, x2, v2):
#   return 'YES' if v1 > v2 and (v2-v1)!= 0 and (x1 - x2) % (v2-v1) == 0 else 'NO'
