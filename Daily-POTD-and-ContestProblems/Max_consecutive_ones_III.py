from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r, zeros, n = 0, 0, 0, len(nums)
        length = 0
        while(r < n):
            if nums[r] == 0: 
                zeros+=1
            if zeros > k:
                if nums[l] == 0:
                    zeros-=1
                l+=1
            r+=1
        return r - l
s = Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))