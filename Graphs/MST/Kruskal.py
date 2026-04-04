class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    # will do path compression
    def findUPar(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]



    def unionBySize(self, u, v):
        ultimate_parent_of_u = self.findUPar(u)
        ultimate_parent_of_v = self.findUPar(v)

        if ultimate_parent_of_u == ultimate_parent_of_v:
            return

        elif self.size[ultimate_parent_of_u] < self.size[ultimate_parent_of_v]:
            self.parent[ultimate_parent_of_u] = ultimate_parent_of_v
            self.size[ultimate_parent_of_v] += self.size[ultimate_parent_of_u]

        elif self.size[ultimate_parent_of_v] < self.size[ultimate_parent_of_u]:
            self.parent[ultimate_parent_of_v] = ultimate_parent_of_u
            self.size[ultimate_parent_of_u] += self.size[ultimate_parent_of_v]

        else:
            self.parent[ultimate_parent_of_v] = ultimate_parent_of_u
            self.size[ultimate_parent_of_u] += self.size[ultimate_parent_of_v]


class Solution:
    def spanningTree(self, V, adj):
        edges = []

        for node in range(V):
            for adjNode, wt in adj[node]:
                edges.append((wt, node, adjNode))

        
        ds = DisjointSet(V)
        edges.sort()

        ans = 0

        for edgeWt, u, v in edges:
            if ds.findUPar(u) != ds.findUPar(v):
                ans += edgeWt
                ds.unionBySize(u, v)

        return ans
