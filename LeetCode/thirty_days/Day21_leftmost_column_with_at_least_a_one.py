'''
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

    BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
    BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
'''

mat =[[0,0], [0,0]]

def leftMostColumnWithOne(binaryMatrix):
    """
    :type binaryMatrix: BinaryMatrix
    :rtype: int
    """
    if len(binaryMatrix) == 0:
        return -1

    row = len(binaryMatrix)
    col = len(binaryMatrix[0])

    out = -1
    m = 0
    n = col - 1

    while (m < row and n >= 0):
        if binaryMatrix[m][n] == 1:
            out = n
            n-=1
        else:
            m+= 1
            
    return out

print(leftMostColumnWithOne(mat))

