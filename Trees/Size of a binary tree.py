class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def sizeofTree(root):
    if root is None:
        return 0
    else:
        ls = sizeofTree(root.left)
        rs = sizeofTree(root.right)
        return ls + rs + 1

root = Node(10)
root.left = Node(20)
root.right = Node(30)
print(sizeofTree(root))