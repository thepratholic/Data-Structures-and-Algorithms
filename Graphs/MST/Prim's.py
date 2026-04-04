import heapq

class Solution:
    def spanningTree(self, V, adj):
        pq = []
        visited = [False] * V 
        sum_ = 0

        heapq.heappush(pq, (0, 0)) # wt, starting_node

        while pq:
            wt, node = heapq.heappop(pq)

            if visited[node]:
                continue

            visited[node] = True
            sum_ += wt

            for adjNode, edgeWt in adj[node]:
                if not visited[adjNode]:
                    heapq.heappush(pq, (edgeWt, adjNode))

        return sum_