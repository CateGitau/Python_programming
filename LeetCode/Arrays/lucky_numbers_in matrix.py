"""
Given a m * n matrix of distinct numbers, 
return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that 
it is the minimum element in its row and maximum in its column.
"""

matrix = [[3,7,8],[9,11,13],[15,16,17]]

for i in range(len(matrix)):
    print(min(matrix[i]))

# min_row = []
#         for r in matrix:
#             min_row.append(min(r))

#         max_col = []
#         for i in range(len(matrix[0])):
#             col = []
#             for j in range(len(matrix)):
#                 col.append(matrix[j][i])
#             max_col.append(max(col))
#         return set(min_row).intersection(set(max_col))

