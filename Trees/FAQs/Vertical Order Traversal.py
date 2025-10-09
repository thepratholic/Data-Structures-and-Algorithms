from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root):
        if not root:
            return []

        q = deque([(root, 0, 0)]) # node, row, column
        column_map = defaultdict(list)

        ans = []

        while q:
            for _ in range(len(q)):
                node, row, column = q.popleft()
                column_map[column].append((row, node.data))

                if node.left:
                    q.append((node.left, row + 1, column - 1))

                if node.right:
                    q.append((node.right, row + 1, column + 1))

        for col in sorted(column_map.keys()):
            column_map[col].sort()
            tmp = []
            for row, val in column_map[col]:
                tmp.append(val)
            ans.append(tmp)

        return ans
