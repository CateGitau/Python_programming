"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
 Letters are case sensitive, so "a" is considered a different type of stone from "A"
"""


J = "aA"
S = "aAAbbbb"

def numJewelsInStones(J, S):
    jewel = []
    for i in J:
        for j in S:
            if i == j:
                jewel.append(j)

    return len(jewel)

print(numJewelsInStones(J, S))


# optimal

def numJewelsInStones(J,S):
    answer = 0
    for i in J:
        answer += S.count(i)
        
    return answer

