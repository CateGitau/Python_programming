# List of Products of all Elements

'''
Implement a function which modifies a list so that each index has a product of all numbers present in the list except the
number stored at that index
'''

arr = [1,2,3,4]

# using nested loop
def find_product(lst):
    result = []
    #stores product of values on the left
    left = 1

    for i in range(len(lst)):
        #stores the product of element in the right
        current_prod = 1
    #loop through the elements on the right of index
        for elem in lst[i+1:]:
            #get product of elements on the right
            current_prod = current_prod * elem
        #append the product of product of pvalues on the left and product of values on the right
        result.append(left * current_prod)

        #update product of values on the left
        left = left * lst[i]

    return result

print(find_product(arr))

'''This algorithm is in O(n^2) because the list is iterated over n(n−1)/2 times.'''

#optimizing the number of multiplications

def find_product(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product


print(find_product([0, 1, 2, 3]))

'''
'''