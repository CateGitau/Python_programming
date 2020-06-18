"""
Given the array candies and the integer extraCandies, 
where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among 
the kids such that he or she can have the greatest number of candies among them.
 Notice that multiple kids can have the greatest number of candies.
"""


candies = [2,3,5,1,3]
extra = 3

def great_candies(candies, extraCandies):
    res = []
    for i in range(len(candies)):
        p = candies[i]+extra
        if p >= max(candies):
            res.append(True)
        else:
            res.append(False)

    return res




print(great_candies(candies, extra))