# Filtering with Lambda Functions

#The filter is another special function that, like map, 
#takes a function and iterables (for example, a list) as inputs. It returns the elements 
# for which the function returns True.

#In this exercise, we will be calculating the sum of all the multiples of 3 or 7 below 1,000


nums = list(range(1000))

filtered = filter(lambda nums: nums % 3 == 0 or nums % 7 == 0, nums)

print(sum(filtered))

