"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.
"""
# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.


text1 = "abcde"
text2 = "ace" 

#more optimal than recursive
def longestCommonSubsequence(text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n,m=len(text1),len(text2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if text1[i]==text2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]



#Recursive 
def longestCommonSubsequence2(text1, text2):
    def helper(i,j):
        if i<0 or j<0:
            return 0
        if text1[i]==text2[j]:
            return helper(i-1,j-1)+1
        return max(helper(i-1,j),helper(i,j-1))
    return helper(len(text1)-1,len(text2)-1)




print(longestCommonSubsequence(text1, text2))
        