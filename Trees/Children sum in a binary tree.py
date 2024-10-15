#User function Template for python3

class Solution:

    def isSumProperty(self, root):
        # code here
        if root is None: return 1
        if not root.left and not root.right:
            return 1

        rightData, leftData = 0, 0

        if root.left is not None:
            leftData = root.left.data

        if root.right is not None:
            rightData = root.right.data

        if root.data == leftData + rightData:
            return self.isSumProperty(root.left) and self.isSumProperty(root.right)
        else: return 0

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

# Check sum property
solution = Solution()
print(solution.isSumProperty(root))