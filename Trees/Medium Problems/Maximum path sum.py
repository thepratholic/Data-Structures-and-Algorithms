# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, maxi):
        if not root:
            return 0

        left_sum = max(0, self.helper(root.left, maxi))
        right_sum = max(0, self.helper(root.right, maxi))

        maxi[0] = max(maxi[0], left_sum + right_sum + root.val)
        return max(left_sum, right_sum) + root.val

    def maxPathSum(self, root):
        maxi = [float("-inf")]
        ans = self.helper(root, maxi)
        return maxi[0]