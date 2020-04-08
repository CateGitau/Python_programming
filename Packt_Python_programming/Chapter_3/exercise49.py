"""
In this exercise, we create a sum_first_n function that sums up the first n integers. For example, 
if we pass the n=3 function, it should return 1 + 2 + 3 = 6:
"""

def sum_first_n(n):
    result = 0
    for i in range(n):
        result+= i+1
    return result

print(sum_first_n(3))