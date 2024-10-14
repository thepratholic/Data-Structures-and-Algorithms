import heapq
import math
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0

        max_heap = [-i for i in nums]

        heapq.heapify(max_heap)

        while k > 0:
            k-=1

            max_ele = -heapq.heappop(max_heap)
            ans += max_ele

            heapq.heappush(max_heap, -math.ceil(max_ele / 3))
        return ans