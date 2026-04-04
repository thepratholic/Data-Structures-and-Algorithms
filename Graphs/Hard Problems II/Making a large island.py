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

    def getSize(self, node):
        return self.size[self.findUPar(node)]

class Solution:
    def isValid(self, i, j, n):
        return i >= 0 and i < n and j >= 0 and j < n 

    def largestIsland(self, grid):
        n = len(grid)
        ds = DisjointSet(n * n)

        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

        # add the initial components by connecting the one's
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0: continue

                for index in range(4):
                    adjr = row + delRow[index]
                    adjc = col + delCol[index]

                    if self.isValid(adjr, adjc, n) and grid[adjr][adjc] == 1:
                        nodeNo = row * n + col
                        adjNodeNo = adjr * n + adjc

                        ds.unionBySize(nodeNo, adjNodeNo)

        
        # make the zero to one and check for the maximum large island
        maximum = float("-inf")

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1: continue

                components_size = set()
                for index in range(4):
                    adjr = row + delRow[index]
                    adjc = col + delCol[index]

                    if self.isValid(adjr, adjc, n) and grid[adjr][adjc] == 1:
                        components_size.add(ds.findUPar(adjr * n + adjc))


                sizeTotal = 0
                for it in components_size:
                    sizeTotal += ds.getSize(it)

                maximum = max(maximum, sizeTotal + 1)

        # the last loop if all the cells in the matrix are 1
        for cell in range(n * n):
            maximum = max(maximum, ds.getSize(cell))

        return maximum
        