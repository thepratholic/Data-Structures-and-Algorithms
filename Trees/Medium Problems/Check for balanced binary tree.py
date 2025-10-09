# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if not root:
            return 0

        lh = self.helper(root.left)
        if lh == -1: 
            return -1

        rh = self.helper(root.right)
        if rh == -1:
            return -1

        if abs(lh - rh) > 1:
            return -1

        return 1 + max(lh, rh)

    def isBalanced(self, root):
        return self.helper(root) != -1