'''
You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. 
Your goal is to form arr by concatenating the arrays in pieces in any order. However, 
you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. 
Otherwise, return false.
'''

arr = [15,88]
pieces = [[88], [15]]


# def canFormArray(arr, pieces):
#     arr_str = "!".join(map(str, arr)) + "!"
#     for p in pieces:
#     return all("!".join(map(str, p))+ "!" in arr_str for p in pieces)

# print(canFormArray(arr, pieces))


numDic = {}
for nums in pieces:
    numid = nums[0]
    numDic[numid] = nums[:]
    
finlist=[]
for i in arr:
    if i in numDic:
        finlist+= numDic[i]

print(finlist == arr)

    
