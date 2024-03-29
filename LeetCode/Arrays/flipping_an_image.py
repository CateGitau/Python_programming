"""
Given a binary matrix A, we want to flip the image horizontally, 
then invert it, and return the resulting image.

To flip an image horizontally means that each row of 
the image is reversed.  For example, flipping [1, 1, 0]
zontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1,
 and each 1 is replaced by 0. For example, inverting
 [0, 1, 1] results in [1, 0, 0].
"""

A = [[1,1,0],[1,0,1],[0,0,0]]

print([[0 if x==1 else 1 for x in x][::-1] for x in A] )

# h = []
# for x in A:
#     h.append(x[::-1])

#     for j in x:
#         if j == 1:
#             j = 0
#         else:
#             j = 1
