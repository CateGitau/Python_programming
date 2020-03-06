#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:26:09 2020

@author: aims
"""

meal_cost = 12
tip_percent = 20
tax_percent = 8

def solve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost*(tip_percent/100))
    #print(tip)
    tax = (meal_cost*(tax_percent/100))
    #print(tax)
    
    print(round(meal_cost + tip + tax))

solve(meal_cost, tip_percent, tax_percent)