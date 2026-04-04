from collections import defaultdict, deque

class Solution:
    def shortestPath(self, edges, N, M):
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        distance = [1e9] * N
        distance[0] = 0

        q = deque()
        q.append(0)  # Only store the node (weight is redundant)

        while q:
            node = q.popleft()

            for adjNode in adj[node]:
                if distance[node] + 1 < distance[adjNode]:
                    distance[adjNode] = distance[node] + 1
                    q.append(adjNode)

        for i in range(N):
            if distance[i] == 1e9:
                distance[i] = -1

        return distance
