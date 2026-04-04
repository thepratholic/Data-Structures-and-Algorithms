class Solution:
    def dfs(self, node, parent, visited, adj):
        visited[node] = True

        for adjNode in adj[node]:
            if not visited[adjNode]:
                if self.dfs(adjNode, node, visited, adj):
                    return True

            elif adjNode != parent:
                return True

        return False

    def isCycle(self, V, adj):
        visited = [False] * V 

        for node in range(V):
            if not visited[node]:
                if self.dfs(node, -1, visited, adj):
                    return True

        return False