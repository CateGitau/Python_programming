# Rearrange Sorted List in Max/Min Form

'''
Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such that the 0th index will have the largest number, 
the 1st index will have the smallest, and the third index will have second-largest, and so on. In other words, all the odd-numbered 
indices will have the largest numbers in the list in descending order and the even-numbered indices will have the smallest numbers in ascending order.
'''

lst = [1,2,3,4,5]

# Solution1 Creating a new list
# Time complexity is O(1)
def max_min(lst):
    result = []
    # iterate half list
    for i in range(len(lst)//2):

        #Append corresponding last element
        result.append(lst[-(i+1)])

        #append the current element:
        result.append(lst[i])

    if len(lst) % 2 ==1:
        #if middle value, then append
        result.append(lst[len(lst)//2])
    return result

print(max_min(lst))

#Solution 2: Using O(1) Extra Space

def max_min(lst):
    # Return empty list for empty list
    if (len(lst) is 0):
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    return lst


