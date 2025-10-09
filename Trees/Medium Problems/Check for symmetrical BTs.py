# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.data != q.data:
            return False

        case1 = self.helper(p.left, q.right)
        case2 = self.helper(p.right, q.left)
        return case1 and case2

    def is_symmetric(self, root):
        if not root:
            return True

        return self.helper(root.left, root.right)
        