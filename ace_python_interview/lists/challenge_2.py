# Merge Two Sorted Lists

'''Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list'''

list1 = [1,3,4,5]  
list2 = [2,6,7,8]

def merge_lists(lst1, lst2):
    ind1 = 0
    ind2 = 0

    while ind1 < len(lst2) and ind2 < len(lst2):
        if lst1[ind1] > lst2[ind2]:
            lst1.insert(ind1, lst2[ind2])

            ind1+=1
            ind2+=1
        else:
            ind1+=1
    
    if ind2 < len(lst2):
        lst1.extend(lst2[ind2:])

    return lst1

print(merge_lists(list1, list2))

'''time complexity is O(m(n+m))O(m(n+m))O(m(n+m)) where n and m are the lengths of the lists. 
Both lists are not traversed separately so we cannot say that complexity is (m+n)(m+n)(m+n). 
The shorter of the two lengths is traversed in the while loop. Also, the insert function gets called when the if-condition is true. 
In the worst-case, the second list has all the elements that are smaller than the elements of the first list. 
In this case, the complexity will be O(mn)O(mn)O(mn). Note that if m > n, we have O(mn)O(mn)O(mn), otherwise the complexity is O(n2n^2n​2​​).'''