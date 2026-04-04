from collections import deque

class Solution:
    def topoSort(self, V, adj):
        indegree = [0] * V 

        for node in range(V):
            for adjNode in adj[node]:
                indegree[adjNode] += 1

        topo = []
        q = deque()

        for node in range(V):
            if indegree[node] == 0:
                q.append(node)

        while q:
            current_node = q.popleft()
            topo.append(current_node)

            for adjNode in adj[current_node]:
                indegree[adjNode] -= 1

                if indegree[adjNode] == 0:
                    q.append(adjNode)

        return topo
