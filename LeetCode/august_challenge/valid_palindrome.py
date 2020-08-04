'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
'''
s = "A man, a plan, a canal: Panama"

def isPalidrome(s):
    fin = []
    for str_ in s:
        if str_.isalnum():
            str_ = str_.lower()
            fin.append(str_)

    return fin == fin[::-1]

    # s = [str_.lower() for str_ in s if str_.isalnum()]
    # return s == s[::-1]


print(isPalidrome(s))

