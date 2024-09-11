class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cnt = 0
        ans = start ^ goal
        for i in range(31):
            if ans & 1 << i:
                cnt += 1
        return cnt

s = Solution()
print(s.minBitFlips(10, 7))
