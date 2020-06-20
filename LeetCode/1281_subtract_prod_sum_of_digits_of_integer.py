"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits. 
"""

n = 234
def subtractProductAndSum(n):
    
    temp = n
    prod = 1
    sums = 0

    
    while(temp != 0):
        prod *= temp % 10
        sums += temp % 10


        temp = int(temp /10)

    print(prod)
    print(sums)
    diff = prod - sums

    return diff


print(subtractProductAndSum(n))
