class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(2)
root.right.right = Node(25)

print(root.data, " ", root.left.data, " ", root.right.data)