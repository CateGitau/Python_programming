"""
Given an array of strings, group anagrams together.

"""
import collections
#Example
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

#my approach
words =  ["eat","tea","tan","ate","nat","bat"]
anagrams = {}
def groupanagrams1(words):
    for i in words:
        sorted_words = "".join(sorted(i))
        if sorted_words in anagrams:
            anagrams[sorted_words].append(i)
        else:
            anagrams[sorted_words] = [i]
        
    return (list(anagrams.values()))
    
    
#Approach 2: Categorize by Sorted String
# Time Complexity: O(N K log K)  where N is the
# length of strings, and K is the maximum length of a string in words. 
# The outer loop has complexity O(N) as we iterate through each string.
# Then, we sort each string in O(K log ⁡K) time.

#Space Complexity: O(NK), the total information content  stored in ans



# Intuition

# Two strings are anagrams if and only if their sorted strings are equal.
#Algorithm

# Maintain a map ans : {String -> List} where each key 
# K is a sorted string, and each value is the list of strings
# from the initial input that when sorted, are equal to K.

# In Python, we will store the key as a hashable tuple, eg. ('c', 'o', 'd', 'e').

def groupAnagrams2(words):
        ans = collections.defaultdict(list)
        for s in words:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


#Approach 3: Categorize by Count
# Intuition

# Two strings are anagrams if and only if their character counts 
# (respective number of occurrences of each character) are the same.

# Algorithm

# We can transform each string s into a character count, count, 
# consisting of 26 non-negative integers representing the number of a's, b's, 
# c's, etc. We use these counts as the basis for our hash map.

def groupAnagrams3(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


# complexity


# Time Complexity: O(NK), where NNN is the length of strs, 
# and K is the maximum length of a string in strs. Counting each string
# is linear in the size of the string, and we count every string.

# Space Complexity: O(NK), the total information content stored in ans.


print(groupAnagrams2(words))
print(groupAnagrams3(words))