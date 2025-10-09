# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, maxi):
        if not root:
            return 0

        lh = self.helper(root.left, maxi)
        rh = self.helper(root.right, maxi)

        maxi[0] = max(maxi[0], lh + rh)
        return max(lh, rh) + 1

    def diameterOfBinaryTree(self, root):
        maxi = [0]
        ans = self.helper(root, maxi)
        return maxi[0]