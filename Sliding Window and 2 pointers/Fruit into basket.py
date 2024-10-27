class Solution:
    def totalFruit(self, fruits):
        n, l, r, maxLen, mpp = len(fruits), 0, 0, 0, {}

        while r < n:
            if fruits[r] in mpp:
                mpp[fruits[r]] += 1
            else:
                mpp[fruits[r]] = 1

            if len(mpp) > 2:
                mpp[fruits[l]] -= 1
                if mpp[fruits[l]] == 0:
                    del mpp[fruits[l]]
                l += 1

            if len(mpp) <= 2:
                maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen

s = Solution()
print(s.totalFruit([1,2,3,2,2]))