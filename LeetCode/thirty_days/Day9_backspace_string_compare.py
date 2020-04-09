"""
Given two strings S and T, return if they are equal when both are typed into empty text editors.
# means a backspace character.
"""

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".

# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".

# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".

# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".

S, T = "ab#c","ad#c"

# Time Complexity: O(M + N)), where M,N  are the lengths of S and T respectively
# Space Complexity: O(M+N).
def backspaceCompare(S, T):
    def build(S):
        ans = []
        for c in S:
            if c != '#':
                ans.append(c)
            elif ans:
                ans.pop()
        return "".join(ans)
    return build(S) == build(T)




#Approach two
#Two pointer
# Iterate through the string in reverse. If we see a backspace 
# character, the next non-backspace character is skipped. 
# If a character isn't skipped, it is part of the final answer.

def backspaceCompare2(self, S, T):
    def F(S):
        skip = 0
        for x in reversed(S):
            if x == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield x

    return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))


print(backspaceCompare(S, T))
          