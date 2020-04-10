# Mapping with Lambda Functions

#map is a special function in Python that applies a 
# given function to all items in a list.

import math
nums = [-3, -5, 1, 4]

print(list(map(lambda x: 1/(1+math.exp(-x)), nums)))