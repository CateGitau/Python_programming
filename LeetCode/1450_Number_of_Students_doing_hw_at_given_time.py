"""
Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. More formally,
return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
"""

startTime = [9,8,7,6,5,4,3,2,1]
endTime = [10,10,10,10,10,10,10,10,10]
queryTime = 5


def busyStudent(startTime, endTime, queryTime):
    students = 0
    for i,j in zip(startTime, endTime):
        for p in range(i, j):
            if p == queryTime:
                students += 1
    return students


print(busyStudent(startTime, endTime, queryTime))



# optimal
def busyStudent2(startTime, endTime, queryTime):
    times = 0
    for (i,n) in zip(startTime,endTime):
            if queryTime <= n and queryTime >= i:
                times += 1
    return times
