'''
Write a function that reverses a string. 
The input string is given as an array of characters char[].

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
'''

s = ["h","e","l","l","o"]

def reverseString(s):
    s[:] = s[::-1]

    return s[:]
print(reverseString(s))
