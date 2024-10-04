class Solution:

    def squareRoot(self, x):
        low, high, ans = 1, x, -1
        while low <= high:
            mid = (low + high) // 2
            mySq = mid * mid
            if mySq == x: return mid
            elif mySq < x:
                low = mid + 1
                ans = mid
            else: high = mid - 1
        return ans

s = Solution()
print(s.squareRoot(16))