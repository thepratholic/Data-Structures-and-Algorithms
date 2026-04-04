import heapq

class Solution:
    def countPaths(self, n, roads):
        MOD = 10 ** 9 + 7
        adj = [[] for _ in range(n)]

        for u, v, wt in roads:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        
        ways = [0] * n 
        ways[0] = 1
        distance = [float("inf")] * n 
        distance[0] = 0
        
        pq = []

        heapq.heappush(pq, (0, 0)) # distance, current_node

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            for adjNode, edgeWt in adj[current_node]:

                if current_distance + edgeWt < distance[adjNode]:
                    distance[adjNode] = current_distance + edgeWt
                    heapq.heappush(pq, (distance[adjNode], adjNode))
                    ways[adjNode] = ways[current_node]

                elif current_distance + edgeWt == distance[adjNode]:
                    ways[adjNode] += ways[current_node] % MOD

        return ways[n - 1] % MOD