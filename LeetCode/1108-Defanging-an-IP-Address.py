#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:57:45 2020

@author: aims
"""

"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""

address = "1.1.1.1"

import re

def defangIPaddr1(address: str):
    return address.replace('.', '[.]')

def defangIPaddr2(address: str):
    return '[.]'.join(address.split('.'))

def defangIPaddr3(address: str):
    return re.sub('\.', '[.]', address)

print(defangIPaddr1(address))
print(defangIPaddr2(address))
print(defangIPaddr3(address))
        
#new = " "
#print (new + "H")