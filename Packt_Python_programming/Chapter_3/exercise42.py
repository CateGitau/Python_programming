"""
A function that will return the second element of a list if it exists
"""
#!/usr/bin/python

lists = [1,2,3]

def get_second_element(lists):
    if len(lists) > 1:
        return lists[1]
    else:
        print("list is too small")
if __name__ == '__main__':
    print(get_second_element(lists))