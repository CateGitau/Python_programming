grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#print(grid)

count = 0
for i in range(len(grid)):
    for j in grid[i]:
        if j < 0:
            count+=1
print(count)
