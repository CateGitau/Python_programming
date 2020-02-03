#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 08:38:17 2020

@author: aims
"""

"""
Given a graph of friends who have different interests, you'd like to know
which groups of friends have the most interests in common. You will then use
a little math to determine a value to return.

You are given integers 'friends_nodes' and 'friends_edges',
representing the number of nodes and edges in the graph respectively. You are
also given three arrays of integers, 'friends_from', 'friends_to' and 
friends_weight' which describe the edges between friends.

The graph consists of nodes numbered consecutively from 1 to 'friends_nodes'.
Any members or groups of members who share the same interest are said to be
connected by that interest(node that two group members can be connected by some
interest even if they are not directly connected by the corresponding edge.)

Once you have determined the node pairs with the maximum number of shared 
interests, return the product of the node pairs' labels. If there are multiple
pairs with the maximum number of shared interests, return the maximum product
among them. 
"""

