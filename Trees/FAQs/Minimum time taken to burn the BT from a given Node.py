from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def markParents(self, root, parent_map, start):
        q = deque([root])
        target = None
        while q:
            node = q.popleft()
            if node.data == start:
                target = node
            if node.left:
                parent_map[node.left] = node
                q.append(node.left)
            
            if node.right:
                parent_map[node.right] = node
                q.append(node.right)
        return target

    def timeToBurnTree(self, root, start):
        if not root:
            return 0

        parent_map = {}
        target = self.markParents(root, parent_map, start)
        if not target:
            return 0

        visited = defaultdict(bool)
        q = deque([target])
        visited[target] = True 
        total_time = 0

        while q:
            size = len(q)
            f = False

            for _ in range(size):
                node = q.popleft()

                if node.left and node.left not in visited:
                    visited[node.left] = True
                    q.append(node.left)
                    f = True

                if node.right and node.right not in visited:
                    visited[node.right] = True
                    q.append(node.right)
                    f = True

                if node in parent_map and parent_map[node] not in visited:
                    visited[parent_map[node]] = True
                    q.append(parent_map[node])
                    f = True

            if f:
                total_time += 1

        return total_time
