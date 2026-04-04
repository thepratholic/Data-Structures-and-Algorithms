class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def findUPar(self, node):
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

        elif self.size[ulp_v] < self.size[ulp_u]:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += 1
    
class Solution:
    def isValid(self, i, j, n, m):
        if i < 0 or i >= n: return False
        if j < 0 or j >= m: return False
        return True

    def numOfIslands(self, n, m, A):
        ds = DisjointSet(n * m)
        visited = [[False] * m for _ in range(n)]

        ans = []
        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]
        count = 0
        for row, col in A:
            if visited[row][col]:
                ans.append(count)
                continue

            visited[row][col] = True
            count += 1

            for i in range(4):
                adjr = row + delRow[i]
                adjc = col + delCol[i]

                if self.isValid(adjr, adjc, n, m) and visited[adjr][adjc]:
                    nodeNo = row * m + col
                    adjNodeNo = adjr * m + adjc

                    if ds.findUPar(nodeNo) != ds.findUPar(adjNodeNo):
                        count -= 1
                        ds.unionBySize(nodeNo, adjNodeNo)

            ans.append(count)

        return ans