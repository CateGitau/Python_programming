#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:45:01 2020

@author: aims
"""


class Person:
    def __init__(self, initialAge):
        if initialAge > 0:
            self.age = initialAge
        else:
            print('Age is not valid, setting age to 0.')
            self.age = 0
            
            
    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif (13 <= self.age) and (self.age <= 18):
            print('You are a teenager.')
        else:
            print('You are old.')
            
    def yearPasses(self):
        self.age += 1
