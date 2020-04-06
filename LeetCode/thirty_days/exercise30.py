"""
we will learn how to access a dictionary using dictionary methods
The goal of the exercise is to print the order values against the 
item while accessing the dictionary by using dictionary methods:
"""

orders = {'apple':5, 'orange':3, 'banana':2}
print(orders.values())
print(list(orders.values()))


# The values() method in this code returns an iterable object. 
# In order to use the values straight away, we can wrap them in a list directly.


print(list(orders.keys()))

# As we can't directly iterate a dictionary, we first convert it to a 
# list of tuples using the items() method, then iterate the resulting 
# list and access it. This is mentioned in the following code snippet:

for tuple in list(orders.items()):
    print(tuple)