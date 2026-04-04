from collections import deque, defaultdict
from typing import List

class Solution:
    def CheapestFlight(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        q = deque()
        adj = defaultdict(list)

        for from_, to, cost in flights:
            adj[from_].append((to, cost))

        distance = [float("inf")] * n 
        distance[src] = 0

        q.append((0, src, 0)) # stops, node, distance

        while q:
            stops, node, dist = q.popleft()

            if stops > K:
                continue

            for adjNode, edgeWt in adj[node]:

                if dist + edgeWt < distance[adjNode] and stops <= K:
                    distance[adjNode] = dist + edgeWt
                    q.append((stops + 1, adjNode, distance[adjNode]))

        
        if distance[dst] == float("inf"):
            return -1

        return distance[dst]