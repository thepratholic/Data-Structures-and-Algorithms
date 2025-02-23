class Solution:
    def f(self, mid, n, m):
        ans = 1
        for i in range(1, n+1):
            ans *= mid
            if (ans > m): return 2
        if ans == m: return 1
        return 0

    def NthRoot(self, n, m):
        ans = 1
        low, high = 1, m 
        while low <= high:
            mid = (low + high) // 2

            val = self.f(mid, n, m)

            if val == 1: return mid

            elif val == 2: high = mid - 1

            else: low = mid + 1

        return -1