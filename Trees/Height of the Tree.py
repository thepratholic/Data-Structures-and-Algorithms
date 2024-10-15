class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def Height(root):
    if root is None:
        return 0
    else:
        lh = Height(root.left)
        rh = Height(root.right)
        return max(lh, rh) + 1

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(100)
print(Height(root))