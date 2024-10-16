class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if root.data == key:
        return root
    elif key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
insert(root, 12)
inorder(root)