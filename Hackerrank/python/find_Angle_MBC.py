#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:59:14 2020

@author: aims
"""

import math
AB = int(input())
BC = int(input())

print(str(int(round(math.degrees(math.atan2(AB,BC)))))+'°')