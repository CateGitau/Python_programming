'''
Given a column title as appear in an Excel sheet, 
return its corresponding column number.
'''
s = "AC"

def titleToNumber(s):
    sum = 0
    for c in s:
        print(c)
        sum = sum * 26 + ord(c) - ord('A') + 1 # ord('A') = 65
    return sum

print(titleToNumber(s))
    