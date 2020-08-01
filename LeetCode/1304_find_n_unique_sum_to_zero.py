'''
Given an integer n, return any array containing n unique integers such that they add up to 0.
'''

n = 5

def sumZero(n):
    L = n//2
    rem = n%2

    if rem!= 0:
        ans = [0]
    else:
        ans = [0]
    for i in range(1, L+1):
        ans.append(-i)
        ans.append(i)
    return ans

print(sumZero(5))