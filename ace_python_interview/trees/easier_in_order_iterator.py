from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# def inorder_iterative(root):
#     result = ""
#     if root ==None:
#         return
    
#     stk = deque()

#     while (len(stk) != 0 or root != None):
#         if root != None:
#             stk.append(root)
#             root = root.left
#             continue
        
#         result += str(stk[-1].value) + ' '
#         root = stk[-1].right
#         stk.pop()

#     return str(result)

def inorder_iterative(root):
    result = ""

    if root == None:
        return
    

    stk = deque()

    while (len(stk)!= 0 or root !=None):
        if root!=None:
            stk.append(root)
            root = root.left
            continue

        result += str(stk[-1].value) + ' '
        root = stk[-1].right
        stk.pop()
    
    return str(result)

root1 = Node(100)
root1.left = Node(50)
root1.left.left = Node(25)
root1.left.right = Node(75)
root1.right = Node(250)
root1.right.left = Node(125)
root1.right.right = Node(300)

print("Inorder Iterator = ", end = "")
print(inorder_iterative(root1))