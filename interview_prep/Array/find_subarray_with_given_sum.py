#Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number. `


arr = [1,4,20,3,10,5]
sum = 33

def subarray(arr, sum):
    n = len(arr)

    for i in range(n):
        curr_sum = arr[i]

        j= i+1
        while j <= n:
            if curr_sum == sum:
                print("the sum is between %d and %d indexes" %(i, j-1))
                return 1

            if curr_sum > sum or j == n:
                break

            curr_sum = curr_sum + arr[j] 

            j+=1

print(subarray(arr, sum))

