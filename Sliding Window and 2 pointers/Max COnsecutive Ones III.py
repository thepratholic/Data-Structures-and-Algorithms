class Solution:
    def longestOnes(self, nums, k):
        n, l, r, maxLen, zeros = len(nums), 0, 0, 0, 0
        while r < n:
            if nums[r] == 0: zeros += 1
            if zeros > k:
                if nums[l] == 0: zeros-=1
                l+=1

            if zeros <= k:
                maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen

s = Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))