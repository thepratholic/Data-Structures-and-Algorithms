from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        q = deque([root])

        cnt = 0
        ans = []
        while q:
            level = []

            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if cnt % 2 == 1:
                level.reverse()
            cnt += 1

            ans.append(level)

        return ans