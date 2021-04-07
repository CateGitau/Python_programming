# Remove Even Integers from List


'''Implement a function that removes all the even elements from a given list'''


my_list = [1,2,4,5,10,6,3]
def remove_even(lst):
    odd_list = []

    for i in lst:
        if i%2 != 0:
            odd_list.append(i)
    return odd_list

print(remove_even(my_list))


#using list comprehension

def remove_even2(lst):
    
    return [i for i in lst if i %2 != 0]

print(remove_even2(my_list))
