# Rearrange Positive and Negative values

'''
Implement a function which rearranges the elements such that all the negative elements appear on the left and positive elements appear on the right of the list.
Note that it tis not necessary to maintain the sorted order of the input list

NB: Zero in this case is trated as a positive integer
'''

my_list = [10,-1,20,4,5,-9,-6]

# My solution Using Auxiliary lists
# O(n)
def rearrange(lst):
    positive = []
    negative = []

    for i in lst:
        if i >= 0:
            positive.append(i)
        else:
            negative.append(i)

    
    return negative + positive

print(rearrange(my_list))


# Rearranging in place
def rearrange2(lst):
    leftMostElelent = 0

    for curr in range(len(lst)):
        if (lst[curr] < 0):
            if (curr is not leftMostElelent):
                lst[curr], lst[leftMostElelent] = lst[leftMostElelent], lst[curr]
            leftMostElelent += 1

    return lst
    

print(rearrange2(my_list))

# Pythonic

def rearrange(lst):
    # get negative and positive list after filter and then merge
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]


print(rearrange([10, -1, 20, 4, 5, -9, -6]))
