from collections import deque

class Solution:
    def isCyclic(self, N, adj):
        indegree = [0] * N 
        q = deque()

        for node in range(N):
            for adjNode in adj[node]:
                indegree[adjNode] += 1

        
        for node in range(N):
            if indegree[node] == 0:
                q.append(node)

        count = 0

        while q:
            current_node = q.popleft()
            count += 1

            for adjNode in adj[current_node]:
                indegree[adjNode] -= 1

                if indegree[adjNode] == 0:
                    q.append(adjNode)

        if count == N:
            return False

        return True