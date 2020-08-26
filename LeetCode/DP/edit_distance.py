'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character
'''

word1 = "horse"
word2 = "ros"

def minDistance(word1, word2):
    """Naive recursive solution"""
    if not word1 and not word2:
        return 0
    if not word1:
        return len(word2)
    if not word2:
        return len(word1)
    if word1[0] == word2[0]:
        return minDistance(word1[1:], word2[1:])
    insert = 1 + minDistance(word1, word2[1:])
    delete = 1 + minDistance(word1[1:], word2)
    replace = 1 + minDistance(word1[1:], word2[1:])
    return min(insert, replace, delete)



print(minDistance(word1, word2))
