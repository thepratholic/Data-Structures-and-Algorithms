# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return None

        cur = root
        newNode = TreeNode(val)

        while cur:
            if cur.data < val:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = newNode
                    break

            else:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = newNode
                    break

        return root
