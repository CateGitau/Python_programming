"""
A happy number is a number defined by the following 
process: Starting with any positive integer, replace 
the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 
(where it will stay), or it loops endlessly in a 
cycle which does not include 1. Those numbers for 
which this process ends in 1 are happy numbers.
"""

num = 2
def isHappy(num):

    n = [int(i)**2 for i in str(num)]
    n_ = sum(n)
    
    if n_ ==1:
        return True
    elif n_ ==4:
        return False
    else:
        return isHappy(n_)

print(isHappy(2))
