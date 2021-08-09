class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def find_min(root):
    if root == None:
        return None

    while root.left != None:
        root = root.left

    return root


def inorder_successor_bst(root, d):
    if root == None:
        return
    
    successor = None

    while root != None:
        if root.value < d:
            root = root.right
        elif root.value > d:
            successor = root
            root = root.left

        else:
            if root.right != None:
                successor = find_min(root.right)
            break
    return successor

root1 = Node(100)
root1.left = Node(50)
root1.left.left = Node(25)
root1.left.right = Node(75)
root1.right = Node(250)
root1.right.left = Node(125)
root1.right.right = Node(300)

d = 75
successor = inorder_successor_bst(root1, d)
print('successor = ', successor.value)


