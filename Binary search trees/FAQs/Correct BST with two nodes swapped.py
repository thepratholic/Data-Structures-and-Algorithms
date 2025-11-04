# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.first = self.middle = self.last = None
        self.previous_node = TreeNode(float("-inf"))

    def inorder(self, root):
        if not root:
            return None

        self.inorder(root.left)

        if self.previous_node and root.data < self.previous_node.data:
            if not self.first:
                self.first = self.previous_node
                self.middle = root
            else:
                self.last = root

        self.previous_node = root
        self.inorder(root.right)

    def recoverTree(self, root):
        if not root:
            return None

        self.first = self.middle = self.last = None
        self.previous_node = TreeNode(float("-inf"))

        self.inorder(root)

        if self.first and self.last:
            self.first.data, self.last.data = self.last.data, self.first.data
        elif self.first and self.middle:
            self.first.data, self.middle.data = self.middle.data, self.first.data

        
        