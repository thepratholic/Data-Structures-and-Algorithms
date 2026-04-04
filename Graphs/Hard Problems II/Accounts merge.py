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
    def accountsMerge(self, accounts):
        n = len(accounts)
        ds = DisjointSet(n)

        mapMailNode = {}

        for node in range(n): # we are assuming every account as node 
            for j in range(1, len(accounts[node])): # here, we are seeing email in each account 
                mail = accounts[node][j]
                
                if mail not in mapMailNode:
                    mapMailNode[mail] = node

                else:
                    ds.unionBySize(node, mapMailNode[mail])

        
        merged_mail = [[] for _ in range(n)]

        for mail, node in mapMailNode.items():
            ultimate_parent = ds.findUPar(node)

            merged_mail[ultimate_parent].append(mail)

        result = []

        for i in range(n):
            if not merged_mail[i]:
                continue

            merged_mail[i].sort()
            temp = [accounts[i][0]] + merged_mail[i]
            result.append(temp) 

        result.sort()
        return result                
