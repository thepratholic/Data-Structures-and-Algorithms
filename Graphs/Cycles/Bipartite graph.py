class Solution:
    def dfs(self, node, col, color, adj):
        color[node] = col

        for adjNode in adj[node]:
            if color[adjNode] == -1:
                if not self.dfs(adjNode, 1 - col, color, adj):
                    return False

            elif color[adjNode] == color[node]:
                return False
        return True
        
    def isBipartite(self, V, adj):
        color = [-1] * V 

        for node in range(V):
            if color[node] == -1:
                if not self.dfs(node, 0, color, adj):
                    return False

        return True