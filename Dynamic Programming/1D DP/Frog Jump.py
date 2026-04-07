class Solution:
    def frogJump(self, heights):
        n = len(heights)
        prev = 0
        prev2 = 0

        for i in range(1, n):
            left = prev + abs(heights[i - 1] - heights[i])
            right = float('inf')
            if i > 1:
                right = prev2 + abs(heights[i - 2] - heights[i])

            cur_i = min(left, right)
            prev2 = prev
            prev = cur_i

        return prev