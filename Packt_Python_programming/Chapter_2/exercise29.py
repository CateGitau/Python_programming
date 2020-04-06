"""
Sometimes, we obtain information from multiple lists. 
For instance, we might have a list to store the names 
of products and another list just to store the quantity of those products. 
What we can do is to aggregate lists using the zip() method.

The zip() method maps a similar index of multiple containers 
so that they can be used just as a single object.
"""

# Using zip() to Manipulate Dictionaries
items = ['apple', 'orange', 'banana']
quantity = [5,3,2]

orders = zip(items, quantity)
print(orders)

#turn zip into a list
orders = zip(items,quantity)
print(list(orders))

#turn zip into tuples
orders = zip(items,quantity)
print(tuple(orders))

# turn zip into dictionaries
orders = zip(items,quantity)
print(dict(orders))

# Did you realize that we have to call orders = zip(items,quantity) every time? 
# In this exercise, you will have noticed that a zip() object is an iterator and,
# therefore, once it has been converted to a list, tuple, or dictionary, 
# it is considered a full iteration and it will not be able to generate any values anymore