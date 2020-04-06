"""
Let's learn how to add and subtract the X and Y matrixes using Python
"""

#create two nested lists, X and Y:
X = [[1,2,3],[4,5,6],[7,8,9]]
Y = [[10,11,12],[13,14,15],[16,17,18]]

# Initialize a result placeholder
result = [[0,0,0], 
        [0,0,0], 
        [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
print(result)