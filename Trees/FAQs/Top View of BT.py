from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def topView(self, root):
        if not root:
            return []

        q = deque([(root, 0)]) # node, column
        column_map = defaultdict(list)

        ans = []

        while q:
            for _ in range(len(q)):
                node, column = q.popleft()
                column_map[column].append(node.data)

                if node.left:
                    q.append((node.left, column - 1))

                if node.right:
                    q.append((node.right, column + 1))

        for col in sorted(column_map.keys()):
            ans.append(column_map[col][0])

        return ans