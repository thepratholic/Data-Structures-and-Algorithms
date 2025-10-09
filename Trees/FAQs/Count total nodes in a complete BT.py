# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def count_nodes(self, root):
        cnt = 0
        if not root:
            return cnt

        q = deque([root])
        while q:
            cnt += len(q)

            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return cnt