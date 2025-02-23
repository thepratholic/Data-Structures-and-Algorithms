class Solution:
    def floorSqrt(self, n: int) -> int:
        low, high = 1, n 

        while low <= high:
            mid = (low + high) // 2

            val = mid * mid

            if val <= n:
                low = mid + 1
            else:
                high = mid - 1

        return high