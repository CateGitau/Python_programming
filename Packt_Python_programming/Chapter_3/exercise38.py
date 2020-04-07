"""
implement the pseudocode to find the maximum from a list of positive numbers:
"""

#creare a list of numbers:
l = [4,2,7,3]
maxim = 0

for i in l:
    if i > maxim:
        maxim = i

print(maxim)