"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time 
(i.e., you must sell the stock before you buy again).
"""


# optimal solution
# Time complexity O(n)
# space complexity (O(1))

price = [1,3,17,180]
max_prof = []
for i in range(len(price[:-1])): 
    #print(i)
    sell = 0
    buy = 0
    if  price[i] > price[i+1]:
        i = i+1
    
    else:
        sell = price[i+1]
        buy = price[i]

        prof = sell - buy
        max_prof.append(prof)
        i = i+2 

print(sum(max_prof))



        