from collections import deque


class Solution:
    def findOrder(self, N, arr):
        indegree = [0] * N  

        adj_list = [[] for _ in range(N)]

        for u, v in arr:
            adj_list[v].append(u)
            indegree[u] += 1

        topo = []
        q = deque()

        for node in range(N):
            if indegree[node] == 0:
                q.append(node)

        while q:
            current_node = q.popleft()
            topo.append(current_node)

            for adjNode in adj_list[current_node]:
                indegree[adjNode] -= 1

                if indegree[adjNode] == 0:
                    q.append(adjNode)

        
        if len(topo) == N: 
            return topo
        else:
            return []