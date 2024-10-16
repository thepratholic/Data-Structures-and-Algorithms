class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)