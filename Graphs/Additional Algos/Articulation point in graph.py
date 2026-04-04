class Solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, vis, tin, low, mark, adj):
        vis[node] = True
        tin[node] = low[node] = self.timer
        self.timer += 1
        child = 0

        for adjNode in adj[node]:
            if adjNode == parent: continue

            if not vis[adjNode]:
                self.dfs(adjNode, node, vis, tin, low, mark, adj)
                low[node] = min(low[node], low[adjNode])

                if low[adjNode] >= tin[node] and parent != -1:
                    mark[node] = True

                child += 1

            else:
                low[node] = min(low[node], tin[adjNode])

        if child > 1 and parent == -1:
            mark[node] = True


    def articulationPoints(self, n, adj):
        vis = [False] * n
        tin = [-1] * n
        low = [-1] * n
        mark = [False] * n
        ans = []

        for node in range(n):
            if not vis[node]:
                self.dfs(node, -1, vis, tin, low, mark, adj)

        for node in range(n):
            if mark[node]:
                ans.append(node)

        if not ans:
            return [-1]
        else:
            return ans