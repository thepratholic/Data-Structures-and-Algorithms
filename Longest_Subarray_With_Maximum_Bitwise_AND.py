from typing import List
class Solution:     
    def longestSubarray(self, nums: List[int]) -> int:

        ans, tally, mx = 0, 0, max(nums)           

        for n in nums:
            if n == mx: tally += 1                 
            else: ans, tally = max(ans, tally), 0   

        return max(ans, tally)                      

s = Solution()
print(s.longestSubarray([1,2,3,3,2,2]))
