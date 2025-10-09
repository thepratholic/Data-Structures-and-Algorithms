# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def getInorder(self, root):
        inorder = []
        if not root:
            return inorder

        cur = root
        while cur:
            if not cur.left:
                inorder.append(cur.data)
                cur = cur.right

            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right

                if prev.right is None:
                    prev.right = cur
                    cur = cur.left

                else:
                    prev.right = None
                    inorder.append(cur.data)
                    cur = cur.right

        return inorder