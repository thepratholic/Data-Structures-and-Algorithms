import heapq

class Solution:
    def shortestPath(self,n, m, edges):
        adj = [[] for _ in range(n + 1)]

        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        pq = []

        parent = list(range(n + 1))
        distance = [float("inf")] * (n + 1)

        distance[1] = 0

        heapq.heappush(pq, (0, 1)) # distance, node

        while pq:
            current_dist, current_node = heapq.heappop(pq)

            for adjNode, edge_wt in adj[current_node]:
                if current_dist + edge_wt < distance[adjNode]:
                    distance[adjNode] = current_dist + edge_wt
                    heapq.heappush(pq, (distance[adjNode], adjNode))
                    parent[adjNode] = current_node

        if distance[n] == float("inf"):
            return [-1]

        ans = []

        node = n 

        while parent[node] != node:
            ans.append(node)
            node = parent[node]

        ans.append(1)
        ans.reverse()

        ans.insert(0, distance[n])

        return ans
        