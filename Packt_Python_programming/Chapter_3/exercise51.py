"""
we create a factorial_iterative function that takes an integer 
and returns the factorial using both an iterative and a recursive approach
"""
#For instance, the factorial of 5 is calculated as 5! = 5 * 4 * 3 * 2 * 1 = 120.

def factorial_iterative(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result

#Note that you can express n! = n * (n – 1)!
def factorial_iterative2(n):
    if n == 1:
        return 1
    else:
        return n* factorial_iterative2(n-1)