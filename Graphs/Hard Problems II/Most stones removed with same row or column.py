
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def findUPar(self, node): # do the path compression
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v: return
        elif self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]

        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def maxRemove(self, stones, n):
        n = len(stones)

        maxRow = maxCol = float("-inf")

        for row, col in stones:
            maxRow = max(maxRow, row)
            maxCol = max(maxCol, col)

        ds = DisjointSet(maxRow + maxCol + 1)

        stone_nodes = set()
        for row, col in stones:
            ds.unionBySize(row, maxRow + col + 1)
            stone_nodes.add(row)
            stone_nodes.add(maxRow + col + 1)

        components = set()
        for it in stone_nodes:
            components.add(ds.findUPar(it))

        return n - len(components)