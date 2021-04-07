'''
Given a string, find the length of the longest 
substring in it with no more than K distinct characters.
'''

string = "araaci"
K = 2


def longestSubstring(string, k):
    maxLength = 0
    windowStart = 0

    char = {}

    for windowEnd in range(len(string)):
        right_char = string[windowEnd]

        if right_char not in char:
            char[right_char] = 0
        char[right_char] += 1

        while len(char) > k:
            left_char = string[windowStart]
            char[left_char] -= 1

            if char[left_char] == 0:
                del char[left_char]
            windowStart += 1
        #remember maximum length so far
        maxLength = max(maxLength, windowEnd-windowStart+1)

    return maxLength

print(longestSubstring(string, K))


