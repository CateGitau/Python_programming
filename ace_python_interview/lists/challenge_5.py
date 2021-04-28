# Find minimum Value in List

'''
Implement a function which finds the smallest number in the given list
'''

arr = [9,2,3,6]

'''
ince the entire list is iterated over once, this algorithm is in linear time, O(n)
'''
#my solution
def findMinimum(lst):
    min_num = lst[0]

    for i in arr:
        if  i < min_num:
            min_num = i

    return min_num

print(findMinimum(arr))


# Sorting the list:(Do not do this in interviews)

def findMinimum2(lst):
    if len(lst)<=0:
        return None
    lst.sort()

    return lst[0]

print(findMinimum2(arr))