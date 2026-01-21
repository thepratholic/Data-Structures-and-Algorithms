class Solution:
    def dfs(self, node, visited, adjacency):
        visited[node] = True

        for adjNode in adjacency[node]:
            if not visited[adjNode]:
                self.dfs(adjNode, visited, adjacency)


    def numProvinces(self, adj):
        V = len(adj)

        adjacency = [[] for _ in range(V)]

        for u in range(V):
            for v in range(V):
                if adj[u][v] == 1:
                    adjacency[u].append(v)
                    adjacency[v].append(u)

        visited = [False] * V 
        count = 0
        for i in range(V):
            if not visited[i]:
                count += 1
                self.dfs(i, visited, adjacency)

        return count