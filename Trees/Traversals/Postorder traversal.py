class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    postorder(root)