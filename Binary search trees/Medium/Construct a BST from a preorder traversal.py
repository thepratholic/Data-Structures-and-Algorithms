# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder):
        i = [0]
        bound = float("inf")
        def helper(i, bound):
            if i[0] == len(preorder) or preorder[i[0]] > bound:
                return None

            root = TreeNode(preorder[i[0]])
            i[0] += 1
            root.left = helper(i, root.data)
            root.right = helper(i, bound)
            return root

        return helper(i, bound)