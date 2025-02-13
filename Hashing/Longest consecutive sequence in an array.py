class Solution:
    def longestConsecutive(self, nums):
        n = len(nums)
        s = set()
        for i in nums:
            s.add(i)

        x, cnt = 0, 0
        longest = 1
        if n == 0: return 0
        for i in s:
            if i - 1 in s: continue
            else:
                x = i 
                cnt = 1
                while x + 1 in s:
                    cnt += 1
                    x += 1
                longest = max(longest, cnt)

        return longest