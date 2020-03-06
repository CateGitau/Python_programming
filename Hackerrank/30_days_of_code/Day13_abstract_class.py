#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 08:00:16 2020

@author: aims
"""

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    price = 0
    def __init__(self, title, author, price):
        super(Book, self).__init__()
        self.price = price

    def display(self):
        print('Title: '+title)
        print('Author: '+author)
        print('Price: '+str(price))





title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()