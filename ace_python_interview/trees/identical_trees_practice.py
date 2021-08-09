class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_identical(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 != None and root2!= None:
        return (root1.value == root2.value and 
        is_identical(root1.left, root2.left) and
        is_identical(root1.right, root2.right))




root1 = Node(100)
root1.left = Node(50)
root1.left.left = Node(25)
root1.right = Node(200)
root1.right.left = Node(250)
root1.right.right = Node(350)


root2= Node(100)
root2.left = Node(50)
root2.left.left = Node(25)
root2.right = Node(200)
root2.right.left = Node(250)
root2.right.right = Node(350)


if is_identical(root1, root2):
    print('are identical')
else:
    print('are not identical')
