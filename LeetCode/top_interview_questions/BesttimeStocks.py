'''
You are given an array prices for which the ith element is the price of a given stock on day i.

Find the maximum profit you can achieve. 
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''

prices = [7,1,5,3,6,4]

def bestTime(prices):
    maxprof = []
    for i in range(len(prices)-1):
        print(i)
        sell = 0
        buy = 0

        if prices[i] > prices[i+1]:
            i+=1
        else:
            sell += prices[i+1]
            buy += prices[i]
            
            maxprof.append(sell - buy)
            i = i+2


    return sum(maxprof)


print(bestTime(prices))