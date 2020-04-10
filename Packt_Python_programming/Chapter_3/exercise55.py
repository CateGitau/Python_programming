"""
Lambda functions are small, anonymous functions that can be defined in a simple one-line syntax:
"""

def add_up(x, y):
    return x+y

print(add_up(2, 5))


# this function can be written using the lambda function sytax:

add_up2 = lambda x, y: x+y
print(add_up2(2,3))

#Note that the main restriction of a lambda function is that it can 
# only contain a single expression

first_item = lambda l: l[0]

l = ['cat', 'dog', 'mouse']

print(first_item(l))