"""
One measure of code efficiency is the actual time taken for your computer to execute it.
There are a few methods with which we can time programs in Python; we will focus on 
using the time module from the standard library
"""

# Timing Your Code
#In this exercise, we will calculate the time taken to 
# execute the function in the previous exercise:

import time
stored_results = {}
def sum_to_n(n):
    start_time = time.perf_counter()
    result = 0
    for i in reversed(range(n)):
        if i + 1 in stored_results:
            print('Stopping sum at %s because we have previously computed it' % str(i + 1))
            result += stored_results[i + 1]
            break
        else:
            result += i + 1
    stored_results[n] = result
    print(time.perf_counter() - start_time, "seconds")
    return result

print(sum_to_n(100))