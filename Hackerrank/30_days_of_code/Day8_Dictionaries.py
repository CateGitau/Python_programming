# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#n = 3
n = int(input())
dicts = {}

for i in range(n):
    names = input()
    vals = names.split(" ")
    dicts[vals[0]] = vals[1]
    #print(dicts)
    
while True:
    try:
        search = input()
        print(search,"+",)
