"""
Given a non-negative integer num, return the number of steps to reduce it to zero. 
If the current number is even, you have to divide it by 2, otherwise, 
you have to subtract 1 from it.
"""

num = 14
def numberOfSteps(num):
    res = []
    res.append(num)
    step = 0

    while res[0] >0:
        if res[0] % 2 == 0:
            res[0] = res[0]//2
        else:
            res[0] = res[0] - 1
        step+= 1

    return step
            

print(numberOfSteps(num))
