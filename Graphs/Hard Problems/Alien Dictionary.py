from collections import deque

class Solution:
    def bfs(self, adj, K):
        indegree = [0] * K
        for node in range(K):
            for adjNode in adj[node]:
                indegree[adjNode] += 1

        
        q = deque()
        for node in range(K):
            if indegree[node] == 0:
                q.append(node)

        topo = []
        while q:
            current_node = q.popleft()
            topo.append(current_node)

            for adjNode in adj[current_node]:
                indegree[adjNode] -= 1

                if indegree[adjNode] == 0:
                    q.append(adjNode)

        return topo

    def findOrder(self, dict, N, K):
        adj = [[] for _ in range(K)]

        for i in range(N - 1):
            s1 = dict[i]
            s2 = dict[i + 1]

            for j in range(min(len(s1), len(s2))):
                if s1[j] != s2[j]:
                    adj[ord(s1[j]) - ord("a")].append(ord(s2[j]) - ord("a"))
                    break


        topo = self.bfs(adj, K)

        ans = ""
        for i in range(K):
            ans += chr(ord("a") + topo[i])
            ans += " "

        return ans