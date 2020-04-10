# Dynamic Programming
# Dynamic programming will help us to address this problem by 
# ensuring we break down the problem into the appropriate subproblems,
# and never solve the same subproblem twice.

"""
we write a sum_to_n function to sum integers up to n. We store the results in a dictionary, 
and the function will use the stored results to return the answer in fewer iterations.
For example, if we already know the sum of integers up to 5 is 15, we should be able to use 
this answer when computing the sum of integers up to 6
"""
    
stored_results = {}

def sum_to_n(n):
    result = 0
    for i in reversed(range(n)):
        result += i + 1
    stored_results[n] = result
    return result

def sum_to_n2(n):
    result = 0
    for i in reversed(range(n)):
        if i + 1 in stored_results:
            print('Stopping sum at %s because we have previously computed it' % str(i + 1))
            result += stored_results[i + 1]
            break
        else:
            result += i + 1
    stored_results[n] = result
    return result

print(sum_to_n2(6))