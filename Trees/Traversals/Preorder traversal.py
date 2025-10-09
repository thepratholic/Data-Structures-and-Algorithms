class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    preorder(root)