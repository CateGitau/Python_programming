"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.
"""


s = "RLRRLLRLRL"

def balancedStringSplit(s):
    res = 0
    cnt = 0

    for i in s:
        if i == 'L':
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            res += 1

    return res

print(balancedStringSplit(s))