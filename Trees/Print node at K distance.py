class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def printNodes(root, k):
    if root is None: return None
    if k == 0: print(root.data, end=" ")
    else:
        printNodes(root.left, k-1)
        printNodes(root.right, k-1)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.right.left = Node(50)

printNodes(root, 2)