'''Given an array of size N-1 such that it can only contain distinct integers in the range of 1 to N. Find the missing element.'''

# n = 5
# arr = [1,2,3,5]

n = 10
arr = {1,2,3,4,5,6,7,8,10}
def missing_num(n, arr):
    for i in range(1, n+1):
        if i not in arr:
            return i


print(missing_num(n, arr))

def missingnum2(n, arr):
    return n*(n+1)//2 - sum(arr)

print(missingnum2(n, arr))