# You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

#     direction can be 0 (for left shift) or 1 (for right shift). 
#     amount is the amount by which string s is to be shifted.
#     A left shift by 1 means remove the first character of s and append it to the end.
#     Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.

# Return the final string after all operations.


# Example 1:

# Input: s = "abc", shift = [[0,1],[1,2]]
# Output: "cab"
# Explanation: 
# [0,1] means shift to left by 1. "abc" -> "bca"
# [1,2] means shift to right by 2. "bca" -> "cab"

# Example 2:

# Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
# Output: "efgabcd"
# Explanation:  
# [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
# [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
# [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
# [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"


s = "abc"
shift = [[0,1], [1,2]]

def stringShift(s, shift):
    n = len(shift)
    while n > 0:
        for i in range(n):
            while shift[i][1] > 0:
                if shift[i][0] == 0:
                #left shift
                
                    s = s + s[0]
                    s = s[1:]

                elif shift[i][0] == 1:
                #right shift
                    s = s[-1] + s
                    s = s[:-1] 

                shift[i][1] -=1
        return s
        n-= 1

print(stringShift(s, shift))


