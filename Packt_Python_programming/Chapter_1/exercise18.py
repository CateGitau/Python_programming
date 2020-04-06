# Calculating perfect Squares
"""
The goal of this exercise is to prompt the user to enter 
a given number and find out whether it is a perfect square.
"""

print("Eneter a number to see if it's a perfect square. ")

number = input()
number = abs(int(number))
i = -1

square = False
while i <= number**(0.5):
    i+=1

    if i*i == number:
        square = True
        break
if square:
    print('The square root of', number, 'is', i, '.')
else:
    print('', number, 'is not a perfect square')
