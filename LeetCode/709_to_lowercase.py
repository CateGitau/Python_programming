'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
'''

input = "Hello"

def toLowerCase(input):
    input = input.lower()
    return input

print(toLowerCase(input))


#correct:
def toLowerCase2(str): 
    return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)

print(toLowerCase2(input))