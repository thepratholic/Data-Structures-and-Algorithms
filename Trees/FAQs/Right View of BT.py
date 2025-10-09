# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            n = len(q)
            for i in range(len(q)):
                node = q.popleft()

                if i == n - 1:
                    ans.append(node.data)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

        return ans