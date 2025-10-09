from collections import defaultdict
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        inMap = defaultdict(int)

        for i in range(len(inorder)):
            inMap[inorder[i]] = i 

        def helper(post_start, post_end, in_start, in_end):
            if post_start > post_end or in_start > in_end:
                return None

            root = TreeNode(postorder[post_end])
            inRoot = inMap[postorder[post_end]]
            numsleft = inRoot - in_start

            root.left = helper(post_start, post_start + numsleft - 1, in_start, inRoot - 1)
            root.right = helper(post_start + numsleft, post_end - 1, inRoot + 1, in_end)

            return root

        return helper(0, len(postorder) - 1, 0, len(inorder) - 1)
