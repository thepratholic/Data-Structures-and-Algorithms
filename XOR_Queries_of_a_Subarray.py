from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        for v in arr:
            prefix_xor.append(prefix_xor[-1] ^ v)
        return [prefix_xor[l] ^ prefix_xor[r+1] for l,r in queries]

s = Solution()
print(s.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))
