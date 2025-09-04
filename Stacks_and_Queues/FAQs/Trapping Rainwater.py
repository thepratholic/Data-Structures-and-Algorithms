class Solution:
    def trap(self, height):
        n = len(height)
        left_max, right_max, total = 0, 0, 0

        l, r = 0, n - 1

        while l < r:
            if height[l] <= height[r]:

                if left_max > height[l]:
                    total += (left_max - height[l])
                else:
                    left_max = height[l]
                l += 1

            else:
                if right_max > height[r]:
                    total += (right_max - height[r])
                else:
                    right_max = height[r]
                r -= 1

        return total