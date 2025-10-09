from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        ans = 0

        q = deque([(root, 0)])
        while q:
            n = len(q)
            minimum_value = q[0][1]
            first, second = -1, -1

            for i in range(n):
                node, cur_id = q.popleft()
                cur_id -= minimum_value

                if i == 0:
                    first = cur_id

                if i == n - 1:
                    last = cur_id

                if node.left:
                    q.append((node.left, 2 * cur_id + 1))

                if node.right:
                    q.append((node.right, 2 * cur_id + 2))

            ans = max(ans, last - first + 1)

        return ans