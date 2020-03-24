"""
On a plane there are n points with integer 
coordinates points[i] = [xi, yi]. Your task is to 
find the minimum time in seconds to visit all points.

You can move according to the next rules:

    In one second always you can either move vertically, 
    horizontally by one unit or diagonally (it means to 
    move one unit vertically and one unit horizontally in one second).
    You have to visit the points in the same order as they appear in the array.

"""

points = [[3,2],[-2,2]]
totalTime = 0
for i in range(len(points) - 1):
    p1 = points[i]
    p2 = points[i+1]

    totalTime += max(abs(p2[1] - p1[1]), abs(p2[0] - p1[0]))
    
print(totalTime)
