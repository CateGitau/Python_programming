#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 08:38:28 2020

@author: aims
"""

"""
You're given a log of daily readings of mercury levels in a river. In each
test case, there are missing mercury values for several of the days. Your task is
to analyze the data and try to identify all of the missing values.

Each row of data contains three whitespace-separated values:
    date, time and the highest reading for that day.
    
There are exactly twenty rows with missing values in each input
file. The missing values are marked as 'missing_1', 'missing_2',
..., missing_20. These missing records have been randomly dispersed in the 
rows of data.

Return a list of all the missing values in order.
NB: All mercury levels are below 400
"""