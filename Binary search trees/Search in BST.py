# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root, val):
        if not root:
            return None

        if root.data == val:
            return root

        if root.data < val:
            return self.searchBST(root.right, val)

        else:
            return self.searchBST(root.left, val)