n = "nnoonn"

def isPalinderome(n):
    new = n[::-1]

    if n == new:
        return True
    else:
        return False

print(isPalinderome(n))
