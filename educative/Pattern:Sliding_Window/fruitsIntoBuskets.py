'''
Given an array of characters where each character represents a fruit tree, 
you are given two baskets, and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit.
'''

'''
Similar Problem : Given a string, find the length of the longest substring in it with at most two distinct characters.
'''
fruit = ['A', 'B', 'C', 'A', 'C']

def fruitsInBusket(fruit):
    busket = {}

    max_length = 0
    windowStart = 0

    for windowEnd in range(len(fruit)):
        right_fruit = fruit[windowEnd]
        if right_fruit not in busket:
            busket[right_fruit] = 0
        busket[right_fruit] += 1

        while len(busket) > 2:
            left_fruit = fruit[windowStart]
            busket[left_fruit] -= 1

            if busket[left_fruit] == 0:
                del busket[left_fruit]
            windowStart += 1 #shrink the window
        max_length = max(max_length, windowEnd-windowStart +1)
        
    return max_length



print(fruitsInBusket(fruit))