'''
Given a binary array, 
find the maximum number of consecutive 1s in this array
'''

input = [1,1,0,1,1,1]

def maxCons(input):

    count = 0
    maxCount = 0

    for num in input:
        if num == 1:
            count+=1
        else:
            maxCount = max(count, maxCount)
            count = 0
    return max(count, maxCount)

print(maxCons(input))


