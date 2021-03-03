'''
Given two strings s and t , 
write a function to determine if t is an anagram of s.
'''

s = "anagram"
t = "nagaram"


def findAnagram(s, t):
    dict1 = {}
    dict2 = {}

    for item in s:
        if item not in dict1:
            dict1[item] = 1
        else:
            dict1[item] +=1
    
    for item in t:
        if item not in dict2:
            dict2[item] = 1
        else:
            dict2[item] +=1
    return dict1 == dict2

print(findAnagram(s, t))