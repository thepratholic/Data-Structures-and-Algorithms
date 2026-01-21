class Solution:
    def dfs(self, node, visited, adj):
        visited[node] = True

        for adjNode in adj[node]:
            if not visited[adjNode]:
                self.dfs(adjNode, visited, adj)

            
    def findNumberOfComponent(self, V, edges):
        visited = [False] * V 

        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = 0

        for i in range(V):
            if not visited[i]:
                count += 1
                self.dfs(i, visited, adj)

        return count