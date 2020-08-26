'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
'''

n = 15

def fizzBuzz(n):
    out = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            out.append("FizzBuzz")
        elif i % 5 == 0:
            out.append("Buzz")
        elif i % 3 == 0:
            out.append("Fizz")
        else:
            out.append(str(i))
    return out

print(fizzBuzz(n))
