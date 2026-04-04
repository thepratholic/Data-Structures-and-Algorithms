from collections import deque

class Solution:
    def canFinish(self, N, arr):
        indegree = [0] * N  

        adj_list = [[] for _ in range(N)]

        for u, v in arr:
            adj_list[v].append(u)
            indegree[u] += 1

        count = 0
        q = deque()

        for node in range(N):
            if indegree[node] == 0:
                q.append(node)

        while q:
            current_node = q.popleft()
            count += 1

            for adjNode in adj_list[current_node]:
                indegree[adjNode] -= 1

                if indegree[adjNode] == 0:
                    q.append(adjNode)

        
        return count == N 