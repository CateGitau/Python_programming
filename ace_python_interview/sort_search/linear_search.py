'''O(n)'''


def linear_search(lst, key):
    if len(lst)<=0:
        return -1

    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1


# Driver code to test above
if __name__ == '__main__':

    lst = [5, 4, 1, 0, 5, 95, 4, -100, 200, 0]
    key = 95

    index = linear_search(lst, key)
    if index != -1:
        print("Key:", key, "is found at index:", index)
    else:
        print(key, " is not found in the list.")