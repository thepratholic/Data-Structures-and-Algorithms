from collections import deque

class Solution:
    def eventualSafeNodes(self, V, adj):
        adj_rev = [[] for _ in range(V)]

        indegree = [0] * V 

        for node in range(V):
            for adjNode in adj[node]:
                adj_rev[adjNode].append(node)
                indegree[node] += 1


        q = deque()

        for node in range(V):
            if indegree[node] == 0:
                q.append(node)

        ans = []

        while q:
            current_node = q.popleft()
            ans.append(current_node)

            for adjNode in adj_rev[current_node]:
                indegree[adjNode] -= 1

                if indegree[adjNode] == 0:
                    q.append(adjNode)

        ans.sort()
        return ans