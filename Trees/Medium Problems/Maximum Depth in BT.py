# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        return max(lh, rh) + 1