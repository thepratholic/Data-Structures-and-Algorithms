# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def get_floor(self, root, key):
        cur = root
        ans = -1
        while cur:  
            if cur.data == key:
                ans = cur.data
                break

            elif cur.data < key:
                ans = cur.data
                cur = cur.right
            else:
                cur = cur.left
        return ans

    def get_ceil(self, root, key):
        cur = root
        ans = -1
        while cur:
            if cur.data == key:
                ans = cur.data
                break
            elif cur.data > key:
                ans = cur.data
                cur = cur.left

            else:
                cur = cur.right
        return ans

    def floorCeilOfBST(self, root, key):
        if not root:
            return [-1, -1]

        floor = self.get_floor(root, key)
        ceil = self.get_ceil(root, key)
        return [floor, ceil]