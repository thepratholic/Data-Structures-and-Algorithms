from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans = arr.copy()
        arr.sort()
        ranks = {}

        for i in arr:
            if i not in ranks:
                ranks[i] = len(ranks) + 1

        for i in range(len(ans)):
            ans[i] = ranks.get(ans[i])

        return ans