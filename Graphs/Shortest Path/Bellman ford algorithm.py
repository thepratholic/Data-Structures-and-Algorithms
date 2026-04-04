class Solution:
    def bellman_ford(self, V, edges, S):
        distance = [int(1e9)] * V 
        distance[S] = 0
        
        for i in range(V - 1):
            for u, v, wt in edges:

                if distance[u] != int(1e9) and distance[u] + wt < distance[v]:
                    distance[v] = distance[u] + wt

        
        for u, v, wt in edges:
            if distance[u] != int(1e9) and distance[u] + wt < distance[v]:
                return [-1]

        return distance