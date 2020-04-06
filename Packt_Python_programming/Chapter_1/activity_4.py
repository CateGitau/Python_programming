"""
Finding the LCM
In this activity, using the following steps, you need to find the LCM of 24 and 36.

The steps are as follows:

Set a pair of variables as equal to 24 and 36.
Initialize the while loop, based on a Boolean that is True by default, with an iterator.
Set up a conditional to check whether the iterator divides both numbers.
Break the while loop when the LCM is found.
Increment the iterator at the end of the loop.
Print the results
"""

a, b = 24, 36

# Find the Least Common Multiple of Two Divisors
counting = True
first_divisor = 24
second_divisor = 36
i = 1
while counting:
    if i % first_divisor == 0 and i % second_divisor == 0:
        print('The Least Common Multiple of', first_divisor, 'and', second_divisor, 'is', i, '.')
        break
    i += 1

