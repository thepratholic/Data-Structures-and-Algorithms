from collections import deque

class Solution:
    def bfs(self, node, adj, visited, ans):
        q = deque()
        q.append(node)

        while q:
            node = q.popleft()
            ans.append(node)

            for adjNode in adj[node]:
                if not visited[adjNode]:
                    visited[adjNode] = True
                    q.append(adjNode)

    def dfs(self, node, adj, visited, ans):
        visited[node] = True
        ans.append(node)

        for adjNode in adj[node]:
            if not visited[adjNode]:
                self.dfs(adjNode, adj, visited, ans)

        
        
    def dfsOfGraph(self, V, adj):
        visited = [False] * V 
        ans = []

        for i in range(V):
            if not visited[i]:
                visited[i] = True
                self.dfs(i, adj, visited, ans)

        return ans

    def bfsOfGraph(self, V, adj):
        visited = [False] * V 
        ans = []
        for i in range(V):
            if not visited[i]:
                visited[i] = True
                self.bfs(i, adj, visited, ans)

        return ans