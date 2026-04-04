from collections import defaultdict

class Solution:
    def __init__(self):
        self.timer = 1

    def criticalConnections(self, V, E):
        vis = [False] * V
        adj = defaultdict(list)

        for u, v in E:
            adj[u].append(v)
            adj[v].append(u)

        tin = [0] * V 
        low = [0] * V
        bridges = []

        def dfs(node, parent):
            vis[node] = True
            tin[node] = low[node] = self.timer
            self.timer += 1

            for it in adj[node]:
                if it == parent: continue

                if not vis[it]:
                    dfs(it, node)
                    low[node] = min(low[node], low[it])

                    if low[it] > tin[node]:
                        # breidges hai yaha pe 
                        bridges.append((node, it))

                else:
                    low[node] = min(low[node], low[it])
 
        dfs(0, -1)
        return bridges
        