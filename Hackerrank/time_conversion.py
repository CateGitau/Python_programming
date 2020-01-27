#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:49:48 2020

@author: aims
"""

"""
Given a time in

-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour 
clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock. 
"""

s = '12:40:22AM'

#print(time.split(':'))

def timeConversion(s):
    #p = s.split(':')
    time_day = s[-2:]
    hr = s[0:2]
    
    if time_day == 'PM' and s[0:2] != '12':
        hr = str(int(s[0:2])+12)
        
    elif time_day == 'AM' and s[0:2] == '12':
        hr = '00'
    
    
    return hr + s[2:-2]
        
    #print(''.join(hr, mm, sec))
    
print(timeConversion(s))            
            

    
    