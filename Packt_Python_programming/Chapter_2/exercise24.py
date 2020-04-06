"""
Let's look at how to use nested lists to perform matrix multiplication for the two matrices shown
"""

X = [[1, 2], [4, 5], [3, 6]]
Y = [[1,2,3,4],[5,6,7,8]]

result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# iterating by row of A 
for i in range(len(X)):   
    # iterating by coloum by B  
    for j in range(len(Y[0])):   
        # iterating by rows of B 
        for k in range(len(Y)): 
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)
