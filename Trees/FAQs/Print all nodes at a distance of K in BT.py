from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def markParents(self, root, parent_map):
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                parent_map[node.left] = node
                q.append(node.left)
            
            if node.right:
                parent_map[node.right] = node
                q.append(node.right)

    def distanceK(self, root, target, k):
        if not root: return []
        parent_map = {}
        self.markParents(root, parent_map)

        visited = defaultdict(bool)
        q = deque([target])
        visited[target] = True
        ans = []
        current_distance = 0

        while q:
            size = len(q)
            if current_distance == k:
                ans.extend(node.data for node in q)
                return ans

            for _ in range(size):
                node = q.popleft()
                if node.left and node.left not in visited:
                    visited[node.left] = True
                    q.append(node.left)

                if node.right and node.right not in visited:
                    visited[node.right] = True
                    q.append(node.right)

                if node in parent_map and parent_map[node] not in visited:
                    visited[parent_map[node]] = True
                    q.append(parent_map[node])

            current_distance += 1

        return ans
