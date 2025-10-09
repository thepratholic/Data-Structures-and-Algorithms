from collections import defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        inMap = defaultdict(int)

        for i in range(len(inorder)):
            inMap[inorder[i]] = i 

        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            root = TreeNode(preorder[pre_start])
            inRoot = inMap[preorder[pre_start]]
            numsleft = inRoot - in_start

            root.left = helper(pre_start + 1, pre_start + numsleft, in_start, inRoot - 1)
            root.right = helper(pre_start + numsleft + 1, pre_end, inRoot + 1, in_end)

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
        