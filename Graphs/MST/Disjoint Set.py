class DisjointSet:
    def __init__(self, n: int):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def findUPar(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    

    def unionBySize(self, u: int, v: int) -> None:
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