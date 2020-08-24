'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
'''


input = [3,1,2,4]

def sortArrayByParity(input):
    fin = []

    for i in input:
        if i % 2 == 0:
            fin.append(i)
    for j in input:
        if j % 2 == 1:
            fin.append(j)

    return fin

print(sortArrayByParity(input))