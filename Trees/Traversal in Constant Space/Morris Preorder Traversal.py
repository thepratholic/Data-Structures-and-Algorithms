# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def preorder(self, root):
        preorder = []

        if not root:
            return preorder

        cur = root
        while cur:
            if not cur.left:
                preorder.append(cur.data)
                cur = cur.right

            else:
                prev = cur.left

                while prev.right and prev.right != cur:
                    prev = prev.right

                if prev.right is None:
                    prev.right = cur
                    preorder.append(cur.data)
                    cur = cur.left

                else:
                    prev.right = None
                    cur = cur.right
        return preorder 
