
from collections import deque

class Solution:
    def shortestPath(self, N, M, edges):

        adj = [[] for _ in range(N)]
        indegree = [0] * N 
        q = deque()

        for u, v, wt in edges:
            adj[u].append((v, wt))
            indegree[v] += 1

        
        for node in range(N):
            if indegree[node] == 0:
                q.append(node)

        ans = []

        while q:
            current_node = q.popleft()
            ans.append(current_node)

            for adjNode, wt in adj[current_node]:
                indegree[adjNode] -= 1

                if indegree[adjNode] == 0:
                    q.append(adjNode)


        distance = [1e9] * N 
        distance[0] = 0
        for node in ans:
            if distance[node] != 1e9:
                for adjNode, weight in adj[node]:
                    if distance[node] + weight < distance[adjNode]:
                        distance[adjNode] = distance[node] + weight

        
        for node in range(N):
            if distance[node] == 1e9:
                distance[node] = -1

        return distance