l = [5,8,1,3,2]

#Bubble Sort Algorithm
# Bubble Sort is a very simple but inefficient sorting algorithm. 
# Its time complexity is O(n^2), meaning that the number of steps 
# required is proportional to the square of the size of the list.
still_swapping = True

while still_swapping:
    still_swapping = False
    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            still_swapping = True
print(l)