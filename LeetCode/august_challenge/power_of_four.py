'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
'''

n = 16

def isPoweroffour(n):
    if n==0:
        return False
    elif n != 1:
        if n % 4 != 0:
            return False
        
    return True
    

print(isPoweroffour(n))