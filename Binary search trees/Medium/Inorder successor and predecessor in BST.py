# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def find_predecessor(self, root, key): # immediate smaller
        ans = -1
        if not root:
            return None

        while root:
            if root.data < key:
                ans = root.data
                root = root.right
            else:
                root = root.left

        return ans

    def find_successor(self, root, key): # immediate larger
        ans = -1
        if not root:
            return -1

        while root:
            if root.data > key:
                ans = root.data
                root = root.left
            else:
                root = root.right

        return ans

    def succPredBST(self, root, key):
        return [self.find_predecessor(root, key), self.find_successor(root, key)]