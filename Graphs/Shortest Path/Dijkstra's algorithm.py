import heapq

class Solution:
    def dijkstra(self, V, adj, S):
        st = []
        distance = [int(1e9)] * V 

        distance[S] = 0

        heapq.heappush(st, (0, S))

        while st:
            dist, node = heapq.heappop(st)

            for adjNode, wt in adj[node]:

                if dist + wt < distance[adjNode]:
                    distance[adjNode] = dist + wt
                    heapq.heappush(st, (distance[adjNode], adjNode))

        return distance
