'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number 
and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.
'''

n = 15

def fizzBuzz(n):
    values = []
        
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            values.append("FizzBuzz")
        elif i % 3 == 0:
            values.append("Fizz")
        elif i % 5 == 0:
            values.append("Buzz")
        else:
            values.append(str(i))
            
    return values

print(fizzBuzz(n))
        