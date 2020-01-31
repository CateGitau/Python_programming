#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:50:44 2020

@author: aims
"""

ride_time = 30
ride_distance = 7
cost_per_minute = [0.2, 0.35, 0.4, 0.45]
cost_per_mile = [1.1, 1.8, 2.3, 3.5]


def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    total_cost = []
    total_cost_pmin = []
    total_cost_pmile = []
    for i in cost_per_minute:
        total_cost_pmin.append(round((i * ride_time), 2))
    
    for k in cost_per_mile:
        total_cost_pmile.append(round((k * ride_distance), 2))
        
    for j, k in zip(total_cost_pmin, total_cost_pmile):
        total_cost.append(j + k)
        
        
        
    return total_cost

print(fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile))