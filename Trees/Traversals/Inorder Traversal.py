class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	# root.left.left = Node(4)
	# root.left.right = Node(5)

	print("\nInorder traversal of binary tree is")
	inorder(root)