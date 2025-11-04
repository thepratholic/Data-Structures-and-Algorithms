# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def lca(self, root, p, q):
        if not root or root.data == p or root.data == q:
            return root

        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)

        if not left:
            return right

        elif not right:
            return left

        else:
            return root