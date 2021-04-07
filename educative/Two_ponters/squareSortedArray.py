'''
Given a sorted array, create a new array containing squares of all the numbers 
of the input array in the sorted order.
'''

arr = [-2, -1, 0, 2, 3]

def squareArray(arr):
    square = []
    for i in arr:
       square.append(i**2)
    return sorted(square)

print(squareArray(arr))



#using two-pointers - space and time complexity is O(N)

def squareArray2(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    highestSquareIdx = n - 1
    left, right = 0, n - 1

    while left <= right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] *arr[right]

        if leftSquare > rightSquare:
            squares[highestSquareIdx] = leftSquare
            left+=1
        else:
            squares[highestSquareIdx] = rightSquare
            right -= 1
        highestSquareIdx -= 1

    return squares

print(squareArray2(arr))

