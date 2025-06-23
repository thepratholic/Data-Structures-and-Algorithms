class Solution:
    def is_possible(self, color_, node, adj, color):
        for adjNode in adj[node]:
            if color[adjNode] == color_:
                return False

        return True

    def solve(self, node, adj, color, n, m):
        if node == n:
            return True

        for color_ in range(1, m + 1):
            if self.is_possible(color_, node, adj, color):
                color[node] = color_

                if self.solve(node + 1, adj, color, n, m):
                    return True

                color[node] = -1

        return False

    def graphColoring(self, edges, m, n):
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        color = [-1] * n
        
        return self.solve(0, adj, color, n, m)