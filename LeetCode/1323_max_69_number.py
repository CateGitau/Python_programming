"""Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""

num = 9669


def maximum69Number(num):
    

    return int(str(num).replace('6', '9', 1))


print(maximum69Number(num))
        
        

