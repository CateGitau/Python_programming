'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way. 
'''


a = "Lowercase"

def detectCapital(a):
    capital = 0
    lower = 0
    length = len(a)

    if a.istitle():
        return True
    else:
        for i in a:
            if i.islower():
                lower+= 1
            else:
                capital+=1
        if capital == length or lower == length:
            return True
        else:
            return False
print(detectCapital(a))


## oooorrrr:

def easiersol(a):
    if a.isupper():
        return True
    elif a[0].isupper() & a[1:].islower():
        return True
    elif a.islower():
        return True
    else:
        return False

