from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxi_or = 0
        for i in nums:
            maxi_or |= i

        total_subsets = 1 << len(nums)
        subs_with_maxi_or = 0

        for i in range(total_subsets+1):
            current_or_value = 0

            for j in range(len(nums)):
                if (i >> j) & 1:
                    current_or_value |= nums[j]

            if current_or_value == maxi_or:
                subs_with_maxi_or += 1

        return subs_with_maxi_or