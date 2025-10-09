class Node:
    def __init__(self, d):
        self.data = d
        self.right = None
        self.left = None

def bfs(root):
    if root is None: return None
    d = []
    d.append(root)
    while len(d) > 0:

        print(d[0].data, end=" ")
        node = d.pop(0)

        if node.left:
            d.append(node.left)
        if node.right:
            d.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

bfs(root)