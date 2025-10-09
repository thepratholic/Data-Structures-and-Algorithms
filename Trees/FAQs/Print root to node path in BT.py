# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def isLeaf(self, root):
        return not root.left and not root.right

    def helper(self, root, ans, curr):
        if not root:
            return

        if self.isLeaf(root):
            curr.append(root.data)
            ans.append(curr[:])
            curr.pop()
            return

        curr.append(root.data)
        self.helper(root.left, ans, curr)
        curr.pop()

        curr.append(root.data)
        self.helper(root.right, ans, curr)
        curr.pop()

    def allRootToLeaf(self, root):
        if not root:
            return []

        ans = []

        self.helper(root, ans, [])
        return ans