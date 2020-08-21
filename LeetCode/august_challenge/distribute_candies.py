candies = 7
num_people = 4



def distributeCandies(candies, num_people):
    arr = [0] * len(range(num_people))
    n = 1
    while candies > 0:
        for i in range(len(arr)):
            if candies >= n:
                arr[i] += n
                candies -= n
                n+=1
            else:
                arr[i] += candies
                candies -= candies
        
    return arr

print(distributeCandies(candies, num_people))