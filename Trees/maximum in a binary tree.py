import math as m
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def maximum(root):
    if root is None: return -m.inf
    else:
        lm = maximum(root.left)
        rm = maximum(root.right)
        return max(root.data, lm, rm)
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
print(maximum(root))