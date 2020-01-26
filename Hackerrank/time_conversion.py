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

s = '07:05:45PM'

#print(time.split(':'))

def timeConversion(s):
    p = s.split(':')
    time_day = p[len(p) - 1].lstrip('123456789')
    vals = p[len(p) - 1][:len(time_day)]
    
    time = []
    
    if time_day == 'PM':
        time.append(str(int(p[0]) + 12))
        time.append(p[1].zfill(2))
        time.append(vals)
        
    else:
        time.append(p[0])
        time.append(p[1])
        
    return (':'.join(time))
        
        

        
    
    #print(''.join(hr, mm, sec))
    
print(timeConversion(s))            
            

    
    